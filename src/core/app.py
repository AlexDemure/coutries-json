import json
from datetime import datetime

from unidecode import unidecode

from src.clients.geonames import GeonamesAlternate
from src.clients.geonames import GeonamesCity
from src.clients.github import GitHubCountry
from src.clients.github import GitHubLanguage
from src.clients.openstreetmaps import OSMCity
from src.clients.stefangabos import StefangabosCountry
from src.clients.stores import StoreCountry
from src.clients.stores import StoreLanguage
from src.crud.cities import CityCRUD
from src.crud.countries import CountryCRUD
from src.crud.countries import CountryLanguageCRUD
from src.crud.geonames import GeonamesAlternateCRUD
from src.crud.geonames import GeonamesCityCRUD
from src.crud.languages import LanguageCRUD
from src.proxy import Proxy
from src.storages.sqlite import get_connection
from src.storages.sqlite import get_cursor
from src.utils import jsonf
from src.utils import multiprocess

from .settings import Settings


def main():
    """
    Шаг №1 - Загрузка справочников из Geonames ~1 мин.
    Шаг №2 - Инициализация таблиц в SQLite ~1-2 сек.
    Шаг №3 - Добавление Geonames-городов в SQLite ~1-2 сек.
    Шаг №4 - Добавление Geonames-альтернативных названий в SQLite ~30 сек.
    Шаг №5 - Добавление Stefangabos-стран с проверкой наличия этих стран в других справочниках в SQLite ~1-2 сек.
    Шаг №6 - Добавление языков на основе стран в SQLite ~1-2 сек.
    Шаг №7 - Создание городов на основе Geonames-городов и Geonames-альтернативных названий в SQLite ~1-2 сек.
    Шаг №8 - Дозаполнения информации по городам из OpenStreetMap ~1 мин на 800 городов с 6 ядрами.
    Шаг №9 - Генерирование выходного файла
    """
    start = datetime.utcnow()

    # Шаг №1 - Загрузка справочников из Geonames ~1 мин.
    GeonamesCity.download()
    multiprocess(GeonamesAlternate.download, iterable=GeonamesAlternate.filenames())

    connection = get_connection()

    #  Шаг №2 - Инициализация таблиц в SQLite
    for crud in [
        CityCRUD,
        CountryCRUD,
        GeonamesCityCRUD,
        GeonamesAlternateCRUD,
        LanguageCRUD,
        CountryLanguageCRUD,
    ]:
        crud.init(get_cursor(connection))

    # Шаг №3 - Добавление Geonames-городов в SQLite
    if not GeonamesCityCRUD.exist(
        get_cursor(connection)
    ):  # Добавление гео-городов из справочника
        cities = GeonamesCity.get(GeonamesCity.filename)

        for city in cities:
            city["id"] = int(city["id"])
            city["country_id"] = city["country_id"].lower()
            GeonamesCityCRUD.add(get_cursor(connection), city)

        connection.commit()

    # Шаг №4 - Добавление Geonames-альтернативных названий в SQLite
    if not GeonamesAlternateCRUD.exist(
        get_cursor(connection)
    ):  # Добавление гео-альтернативных названий
        countries = GeonamesCityCRUD.get_list_country_id(get_cursor(connection))

        for country in countries:
            cities = GeonamesCityCRUD.get_list_by_country(
                get_cursor(connection), country["country_id"]
            )

            alternates = GeonamesAlternate.get(
                filename=country["country_id"].upper(),
                city_ids=[city["id"] for city in cities],
            )

            for alternate in alternates:
                alternate["city_id"] = int(alternate["city_id"])
                GeonamesAlternateCRUD.add(get_cursor(connection), alternate)

        connection.commit()

    # Шаг №5 - Добавление Stefangabos-стран в SQLite с проверкой наличия этих стран в других справочниках
    if not CountryCRUD.exist(get_cursor(connection)):
        store_countries_ids = set(country["id"] for country in StoreCountry.get())

        github_countries_ids = set(country["id"] for country in GitHubCountry.get())

        stegangabos_countries = StefangabosCountry.get()

        for country in stegangabos_countries:
            if (country["id"] in store_countries_ids) or (
                country["id"] in github_countries_ids
            ):
                CountryCRUD.add(get_cursor(connection), country)

        connection.commit()

    # Шаг №6 - Добавление языков в SQLite на основе стран
    if not LanguageCRUD.exist(get_cursor(connection)) or not CountryLanguageCRUD.exist(
        get_cursor(connection)
    ):
        country_ids = set(
            country["id"]
            for country in CountryCRUD.get_list_ids(get_cursor(connection))
        )

        store_languages = {language["id"]: language for language in StoreLanguage.get()}
        store_countries = {
            country["id"]: country["languages"]
            for country in StoreCountry.get()
            if country["id"] in country_ids
        }

        github_languages = {
            language["id"]: language for language in GitHubLanguage.get()
        }
        github_countries = {
            country["id"]: country["languages"]
            for country in GitHubCountry.get()
            if country["id"] in country_ids
        }

        for country_id in country_ids:
            store_language_codes = store_countries.get(country_id)

            github_language_codes = github_countries.get(country_id)

            languages = list()

            if store_language_codes:
                for language_code in store_language_codes:  # en, ru
                    if store_languages.get(language_code):
                        if github_languages.get(language_code):
                            store_languages[language_code]["origin"] = github_languages[
                                language_code
                            ]["origin"]
                        languages.append(store_languages[language_code])

            elif github_language_codes:
                for language_code in github_language_codes:  # en, ru
                    if github_languages.get(language_code):
                        languages.append(github_languages[language_code])
                    else:
                        languages.append(github_languages["en"])

            else:
                languages.append(github_languages["en"])

            for language in languages:
                if not LanguageCRUD.get(get_cursor(connection), "id", language["id"]):
                    LanguageCRUD.add(get_cursor(connection), language)

                if not CountryLanguageCRUD.get_by_fields(
                    get_cursor(connection),
                    language_id=language["id"],
                    country_id=country_id,
                ):
                    CountryLanguageCRUD.add(
                        get_cursor(connection),
                        dict(country_id=country_id, language_id=language["id"]),
                    )

        connection.commit()

    # Шаг №7 - Создание городов на основке Geonames-городов и Geonames-альтернативных названий в SQLite
    if not CityCRUD.exist(get_cursor(connection)):
        countries = GeonamesCityCRUD.get_list_country_id(get_cursor(connection))

        for country in countries:
            cities = GeonamesCityCRUD.get_list_by_country(
                get_cursor(connection), country["country_id"]
            )

            for city in cities:
                _city = dict(
                    id=city["id"],
                    country_id=country["country_id"],
                    origin=city["name"],
                    ascii=city["asciiname"],
                )

                alternates = GeonamesAlternateCRUD.get_list_by_city(
                    get_cursor(connection), _city["id"]
                )

                for language in Settings.AVAILABLE_LANGUAGES:
                    language_alternates = [
                        item for item in alternates if item["language_id"] == language
                    ]

                    if language_alternates:
                        preferred_alternates = [
                            item
                            for item in language_alternates
                            if item["is_preferred_name"] == "1"
                        ]
                        if preferred_alternates:
                            assert len(preferred_alternates) == 1, preferred_alternates
                            _city[language] = preferred_alternates[0]["alternate_name"]
                        else:
                            _city[language] = language_alternates[0]["alternate_name"]

                    if language == "en":
                        if _city.get(language):
                            _city[language] = unidecode(_city[language])

                CityCRUD.add(get_cursor(connection), _city)

        connection.commit()

    # Шаг №8 - Дозаполнения информации по городам из OpenStreetMap
    if Settings.PROXY:
        proxy = Proxy()
    else:
        proxy = None

    cities = CityCRUD.get_list_without_translation(get_cursor(connection))

    update_cities = multiprocess(OSMCity.get, proxy, iterable=cities)

    for city in update_cities:
        if city["updated_fields"]:
            CityCRUD.update(
                get_cursor(connection),
                key="id",
                value=city["id"],
                **city["updated_fields"],
            )

    connection.commit()

    # Шаг №9 - Генерирование выходного файла
    prepared_countries = list()

    countries = CountryCRUD.get_list(get_cursor(connection))

    for country in countries:
        cities = CityCRUD.get_list_by_country(get_cursor(connection), country["id"])

        languages = LanguageCRUD.get_list_by_country(
            get_cursor(connection), country["id"]
        )

        prepared_countries.append(dict(**country, languages=languages, cities=cities))

    with open(jsonf(Settings.RETURN_FILENAME), "w") as file:
        file.write(
            json.dumps(
                prepared_countries,
                sort_keys=False,
                indent=4,
                separators=(",", ": "),
                ensure_ascii=False,
            )
        )

    print(
        f"[Main] Finish collect countries count: {len(prepared_countries)} seconds: {(datetime.utcnow() - start).seconds}"
    )


if __name__ == "__main__":
    main()
