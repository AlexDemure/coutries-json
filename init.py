import csv
import json
import os
import re
import sqlite3
from collections import Counter

from datetime import datetime
from io import BytesIO
from pathlib import Path
from typing import Any
from typing import Optional
from zipfile import ZipFile

import requests
from bs4 import BeautifulSoup
from requests.auth import HTTPProxyAuth
from unidecode import unidecode
from geonames import GeonamesCity, GeonamesAlternate
from crud import CityCRUD, CountryCRUD, GeonamesCityCRUD, GeonamesAlternateCRUD, LanguageCRUD, get_cursor, get_connection
from settings import Settings
from proxy import Proxy
from utils import multiprocess
from openstreetmaps import OSMCity



class Collector:
    countries_filename: str = None
    languages_filename: str = None

    @staticmethod
    def default_language() -> dict:
        return {
            "name": "English (International)",
            "code": "en",
            "native": "English"
        }

    @staticmethod
    def to_list(string: str) -> list[str]:
        return string.replace(' ', '').replace('-', '').split(',')

    @classmethod
    def read(cls, filename: str) -> list[dict]:
        with open(filename, "r") as file:
            return json.loads(file.read())

    @classmethod
    def get_countries(cls) -> list[dict]:
        return cls.read(cls.countries_filename)

    @classmethod
    def get_languages(cls) -> list[dict]:
        return cls.read(cls.languages_filename)

    @classmethod
    def get_country_by_code(cls, countries: list[dict], code: str) -> Optional[dict]:
        raise NotImplementedError


class GitHub(Collector):
    countries_filename: str = "countries_github.json"
    languages_filename: str = "languages_github.json"

    @classmethod
    def get_country_by_code(cls, countries: list[dict], code: str) -> Optional[dict]:
        for item in countries:
            if item['country_code_name'].lower() == code.lower():
                return item

    @classmethod
    def get_language_by_code(cls, languages: list[dict], code: str) -> Optional[dict]:
        for item in languages:
            if item['code'].lower() == code.lower():
                return item


class Appstore(Collector):
    countries_filename: str = "countries_appstore.json"
    languages_filename: str = "languages_appstore.json"

    @classmethod
    def get_country_by_code(cls, countries: list[dict], code: str) -> Optional[dict]:
        for item in countries:
            if item['Country code'].lower() == code.lower():
                return item

    @classmethod
    def get_language_codes_by_country(cls, country: dict) -> list[str]:

        ios_languages = cls.to_list(country['iOS languages'])

        android_languages = cls.to_list(country['Android languages'])

        return list(set(ios_languages + android_languages))

    @classmethod
    def get_language_by_code(cls, languages: list[dict], code: str) -> Optional[dict]:
        for item in languages:
            if item['Language code '].lower() == code.lower():
                return item


class World(Collector):
    countries_filename: str = "countries_world.json"



def main():
    """
    Шаг №1 - Загрузка справочников из Geonames ~1 мин.
    Шаг №2 - Инициализация таблиц в SQLite ~1-2 сек.
    Шаг №3 - Добавление Geonames-городов в SQLite ~1-2 сек.
    Шаг №4 - Добавление Geonames-альтернативных названий в SQLite ~30 сек.
    Шаг №5 - Создание городов на основе Geonames-городов и Geonames-альтернативных названий в SQLite ~1-2 сек.
    Шаг №6 - Дозаполнения информации по городам из OpenStreetMap ~1 мин на 800 городов.

    """
    start = datetime.utcnow()

    # Шаг №1 - Загрузка справочников из Geonames ~1 мин.
    GeonamesCity.download()
    multiprocess(GeonamesAlternate.download, iterable=GeonamesAlternate.filenames())

    connection = get_connection()

    #  Шаг №2 - Инициализация таблиц в SQLite
    for crud in [CityCRUD, CountryCRUD, GeonamesCityCRUD, GeonamesAlternateCRUD, LanguageCRUD]:
        crud.init(get_cursor(connection))

    # Шаг №3 - Добавление Geonames-городов в SQLite
    if not GeonamesCityCRUD.exist(get_cursor(connection)):  # Добавление гео-городов из справочника

        cities = GeonamesCity.get(GeonamesCity.filename)

        for city in cities:
            city['id'] = int(city['id'])
            city['country_id'] = city['country_id'].lower()
            GeonamesCityCRUD.add(get_cursor(connection), city)

        connection.commit()

    # Шаг №4 - Добавление Geonames-альтернативных названий в SQLite
    if not GeonamesAlternateCRUD.exist(get_cursor(connection)):  # Добавление гео-альтернативных названий

        countries = GeonamesCityCRUD.get_list_country_id(get_cursor(connection))

        for country in countries:

            cities = GeonamesCityCRUD.get_list_by_country(get_cursor(connection), country['country_id'])

            alternates = GeonamesAlternate.get(
                filename=country['country_id'].upper(),
                city_ids=[city['id'] for city in cities],
            )

            for alternate in alternates:
                alternate['city_id'] = int(alternate['city_id'])
                GeonamesAlternateCRUD.add(get_cursor(connection), alternate)

        connection.commit()

    # Шаг №5 - Создание городов на основке Geonames-городов и Geonames-альтернативных названий в SQLite
    if not CityCRUD.exist(get_cursor(connection)):

        countries = GeonamesCityCRUD.get_list_country_id(get_cursor(connection))

        for country in countries:

            cities = GeonamesCityCRUD.get_list_by_country(get_cursor(connection), country['country_id'])

            for city in cities:

                _city = dict(
                    id=city['id'],
                    country_id=country['country_id'],
                    origin=city['name'],
                    ascii=city['asciiname']
                )

                alternates = GeonamesAlternateCRUD.get_list_by_city(get_cursor(connection), _city['id'])

                for language in Settings.AVAILABLE_LANGUAGES:

                    language_alternates = [item for item in alternates if item['language_id'] == language]

                    if language_alternates:
                        preferred_alternates = [item for item in language_alternates if item['is_preferred_name'] == '1']
                        if preferred_alternates:
                            assert len(preferred_alternates) == 1, preferred_alternates
                            _city[language] = preferred_alternates[0]['alternate_name']
                        else:
                            _city[language] = language_alternates[0]['alternate_name']

                    if language == 'en':
                        if _city.get(language):
                            _city[language] = unidecode(_city[language])

                CityCRUD.add(get_cursor(connection), _city)

        connection.commit()

    # Шаг №6 - Дозаполнения информации по городам из OpenStreetMap
    proxy = Proxy()

    cities = CityCRUD.get_list_without_translation(get_cursor(connection))

    update_cities = multiprocess(OSMCity.get, proxy, iterable=cities)

    for city in update_cities:
        if city['updated_fields']:
            CityCRUD.update(get_cursor(connection), key='id', value=city['id'], **city['updated_fields'])

    connection.commit()

    #
    # prepared_countries = []
    #
    # for item in countries_world:
    #
    #     language_codes = []
    #
    #     country = Appstore.get_country_by_code(countries_appstore, item['alpha2'])
    #     if country:
    #         language_codes = Appstore.get_language_codes_by_country(country)
    #
    #     if not country:
    #         country = GitHub.get_country_by_code(countries_github, item['alpha2'])
    #         if country:
    #             language_codes = Collector.to_list(country.get('lang_code', ''))
    #
    #     if not country:
    #         print(f'Not found country:{item}')
    #         continue
    #
    #     languages = []
    #
    #     for code in language_codes:
    #         if code:
    #             language = Appstore.get_language_by_code(languages_appstore, code)
    #             native_language = GitHub.get_language_by_code(languages_github, code)
    #
    #             if not language and not native_language:
    #                 print(f"Language not found: {code}: {country}")
    #                 continue
    #
    #             if language:
    #                 languages.append(
    #                     dict(
    #                         name=language['Language name '].capitalize(),
    #                         code=language['Language code '],
    #                         native=native_language['nativeName'].capitalize() if native_language else None
    #                     )
    #                 )
    #             else:
    #                 languages.append(
    #                     dict(
    #                         name=native_language['name'].capitalize(),
    #                         code=native_language['code'],
    #                         native=native_language['nativeName'].capitalize() if native_language else None
    #                     )
    #                 )
    #
    #     prepared_country = dict(
    #         iso=item['id'],
    #         id=item['alpha2'],
    #         en=item['en'].capitalize(),
    #         ru=item['ru'].capitalize(),
    #         languages=languages if languages else [Collector.default_language()],
    #         cities=cities_db.get_list_by_country(item['alpha2'])
    #     )
    #
    #     prepared_countries.append(prepared_country)
    #
    # with open("result2.json", "w") as file:
    #     file.write(json.dumps(
    #             prepared_countries,
    #             sort_keys=False,
    #             indent=4,
    #             separators=(',', ': '),
    #             ensure_ascii=False
    #         )
    #     )

    print("End", (datetime.utcnow() - start).seconds)


if __name__ == '__main__':
    main()
