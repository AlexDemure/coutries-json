import csv
import json
from io import BytesIO
from typing import Optional
from zipfile import ZipFile
import sqlite3

import requests
import tempfile


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


def processing() -> None:

    countries_world = World.get_countries()
    countries_github = GitHub.get_countries()
    countries_appstore = Appstore.get_countries()
    languages_appstore = Appstore.get_languages()
    languages_github = GitHub.get_languages()

    prepared_countries = []

    for item in countries_world:

        language_codes = []

        country = Appstore.get_country_by_code(countries_appstore, item['alpha2'])
        if country:
            language_codes = Appstore.get_language_codes_by_country(country)

        if not country:
            country = GitHub.get_country_by_code(countries_github, item['alpha2'])
            if country:
                language_codes = Collector.to_list(country.get('lang_code', ''))

        if not country:
            print(f'Not found country:{item}')
            continue

        languages = []

        for code in language_codes:
            if code:
                language = Appstore.get_language_by_code(languages_appstore, code)
                native_language = GitHub.get_language_by_code(languages_github, code)

                if not language and not native_language:
                    print(f"Language not found: {code}: {country}")
                    continue

                if language:
                    languages.append(
                        dict(
                            name=language['Language name '].capitalize(),
                            code=language['Language code '],
                            native=native_language['nativeName'].capitalize() if native_language else None
                        )
                    )
                else:
                    languages.append(
                        dict(
                            name=native_language['name'].capitalize(),
                            code=native_language['code'],
                            native=native_language['nativeName'].capitalize() if native_language else None
                        )
                    )

        prepared_country = dict(
            country_iso=item['id'],
            country_code=item['alpha2'],
            country_en=item['en'].capitalize(),
            country_ru=item['ru'].capitalize(),
            languages=languages if languages else [Collector.default_language()]
        )

        cities = []

        filename = prepared_country['country_code'].upper()

        data = requests.get(
            f"https://download.geonames.org/export/dump/alternatenames/{filename}.zip"
        )

        archive = ZipFile(BytesIO(data.content))

        archive.extract(f'{filename}.txt', '')

        prepared = Prepared(filename=filename, fields=('alternateNameId', 'geonameid', 'isolanguage', 'alternateName'))

        rows = prepared.read()

        prepared.to_csv(rows)

        prepared.csv_to_json()


        print("Preperade country:", prepared_country)

        prepared_countries.append(prepared_country)

    with open("result2.json", "w") as file:
        file.write(json.dumps(prepared_countries, ensure_ascii=False))


class Prepared:

    filename: str = None
    fields: tuple[str] = None

    def __init__(self, filename: str, fields: tuple[str]) -> None:
        self.filename = filename
        self.fields = fields


    def read(self) -> list[str]:
        with open(f"{self.filename}.txt", 'r') as file:
            reader = csv.reader(file, delimiter='\t')
            return list(reader)


    def to_csv(self, rows: list[str]) -> None:
        with open(f'{self.filename}.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerow(self.fields)
            writer.writerows(rows)

    def csv_to_json(self):
        csv_rows = []

        with open(f'{self.filename}.csv', 'r') as file:
            reader = csv.DictReader(file)
            field = reader.fieldnames
            for row in reader:
                csv_rows.extend(
                    [
                        {
                            field[i]: row[field[i]] for i in range(len(field))
                        }
                    ]
                )

        with open(f'{self.filename}.json', 'w') as file:
            file.write(
                json.dumps(
                    csv_rows,
                    sort_keys=False,
                    indent=4,
                    separators=(',', ': '),
                    ensure_ascii=False)
            )  # for pretty


class Cities(Prepared):
    ...

class Alternames(Prepared):
    filename = "RU"
    fields = ('alternateNameId', 'geonameid', 'isolanguage', 'alternateName')

data = requests.get("https://download.geonames.org/export/dump/alternatenames/RU.zip")
archive = ZipFile(BytesIO(data.content))
archive.extract('RU.txt', '')

rows = Alternames.read()
Alternames.to_csv(rows)
Alternames.csv_to_json()


"https://download.geonames.org/export/dump/cities15000.zip"

cities = Cities(
    filename="cities15000",
    fields=('geonameid', 'name', 'asciiname', 'alternatenames', 'latitude', 'longitude', 'featureClass', 'featureCode', 'countryCode')
)
rows = cities.read()
cities.to_csv(rows)
cities.csv_to_json()

prepared_country_with_cities = dict()

with open('cities15000.json', mode='r') as file:
    cities = json.loads(file.read())

for city in cities:
    key = city['countryCode'].lower()
    if not prepared_country_with_cities.get(key):
        prepared_country_with_cities[key] = []

    prepared_country_with_cities[key].append(
        dict(
            id=city['geonameid'],
            name=city['name']
        )
    )

with open('country_with_cities.json', mode='w') as file:
    file.write(
        json.dumps(
            prepared_country_with_cities,
            sort_keys=False,
            indent=4,
            separators=(',', ': '),
            ensure_ascii=False
        )
    )

with open('country_with_cities.json', mode='r') as file:
    countries: dict[str, list] = json.loads(file.read())

prepared_countries = dict()

for country, cities in countries.items():
    print(country, cities, "\n")
    # i = input(f"Скачать архив для {country} ?")

    Этап - Скачивание TXT
    data = requests.get(f"https://download.geonames.org/export/dump/alternatenames/{country.upper()}.zip")
    print(data.status_code)
    archive = ZipFile(BytesIO(data.content))
    archive.extract(f'{country.upper()}.txt', '')

    Этап - Генерирование TXT -> JSON
    prepared = Prepared(
        filename=country.upper(),
        fields=('alternateNameId', 'geonameid', 'isolanguage', 'alternateName')
    )
    rows = prepared.read()
    prepared.to_csv(rows)
    prepared.csv_to_json()

    with open(f'{country.upper()}.json', mode='r') as file:
        country_cities: list[dict] = json.loads(file.read())

    for city in cities:
        _cities = [item for item in country_cities if item['geonameid'] == city['id'] and item['isolanguage'] in ['en', 'ru']]

        if not prepared_countries.get(country):
            prepared_countries[country] = []

        prepared_countries[country].append(
            dict(
                id=city['id'],
                name=city['name'],
                cities=_cities
            )
        )

with open('country_with_cities2.json', mode='w') as file:
    file.write(
        json.dumps(
            prepared_countries,
            sort_keys=False,
            indent=4,
            separators=(',', ': '),
            ensure_ascii=False
        )
    )


class Geonames:

    download_url: str = "https://download.geonames.org/export/dump"

    cities_filename: str = "cities15000"

    @classmethod
    def get_cities(cls) -> list[dict]:

        response = requests.get(f"{cls.download_url}/{cls.cities_filename}.zip")

        archive = ZipFile(BytesIO(response.content))

        file = archive.read(f'{cls.cities_filename}.txt').decode()

        rows = list(csv.reader(file.split("\n"), delimiter='\t'))

        keys = (
            "geonameid",
            "name",
            "asciiname",
            "alternate_names",
            "latitude",
            "longitude",
            "feature_class",
            "feature_code",
            "country_code",
        )

        prepared_rows = []

        for row in rows:

            raw_dict = dict()

            try:
                for index, key in enumerate(keys):
                    raw_dict[key] = row[index]
            except IndexError:
                print("INDEX ERROR", row)
                continue

            prepared_rows.append(
                dict(
                    id=int(raw_dict['geonameid']),
                    country_id=raw_dict['country_code'].lower(),
                    en=raw_dict['name'],
                    ru=None,
                )
            )

        return prepared_rows

    @classmethod
    def get_alter_names(cls, country: str, city_ids: list[int]) -> list[dict]:

        response = requests.get(f"{cls.download_url}/alternatenames/{country}.zip")

        archive = ZipFile(BytesIO(response.content))

        file = archive.read(f'{country}.txt').decode()

        rows = list(csv.reader(file.split("\n"), delimiter='\t'))

        keys = (
            "alternateNameId",
            "geonameid",
            "isolanguage",
            "alternate_name",
            "isPreferredName",
            "isShortName",
            "isColloquial",
            "isHistoric",
        )

        # row[4] and int(row[4]) == 1
        rows = [row for row in rows if row and int(row[1]) in city_ids and row[2] and row[2] in ['ru'] and not row[7]]

        prepared_rows = []

        for row in rows:

            raw_dict = dict()

            try:
                for index, key in enumerate(keys):
                    raw_dict[key] = row[index]
            except IndexError:
                print("INDEX ERROR", row)
                continue

            prepared_rows.append(
                dict(
                    id=int(raw_dict['geonameid']),
                    language_id=raw_dict['isolanguage'].lower(),
                    name=raw_dict['alternate_name'],
                    isPreferredName=raw_dict['isPreferredName'],
                    isShortName=raw_dict['isShortName'],
                    isColloquial=raw_dict['isColloquial'],
                    isHistoric=raw_dict['isHistoric'],
                )
            )
        return prepared_rows


class Collector:

    db: str = "countries.db"

    connection: sqlite3.Connection = None

    @classmethod
    def init_db(cls, cursor: sqlite3.Cursor) -> None:
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS
            cities(id, country_id, en, ru)
            """
        )

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS
            alternames(id, language_id, name, isPreferredName, isShortName, isColloquial, isHistoric)
            """
        )

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS
            alternate(alternateNameId, geonameid, isolanguage, alternate_name, isPreferredName, isShortName, isColloquial, isHistoric)
            """
        )

    @classmethod
    def processing(cls):

        cls.connection: sqlite3.Connection = sqlite3.connect(cls.db)

        cursor = cls.connection.cursor()

        cls.init_db(cursor)

        cities = Geonames.get_cities()

        for city in cities:

            columns = ', '.join(city.keys())

            placeholders = ':' + ', :'.join(city.keys())

            query = 'INSERT OR IGNORE INTO cities (%s) VALUES (%s)' % (columns, placeholders)

            cursor.execute(query, city)

        cls.connection.commit()

        countries = cursor.execute("select country_id from cities group by country_id").fetchall()

        for country in countries:

            city_ids = cursor.execute(f"select cities.id from cities where cities.country_id == '{country[0]}'").fetchall()

            city_ids = [item[0] for item in city_ids]

            if not city_ids:
                print("NOT CITIES", country)
                continue

            alternames = Geonames.get_alter_names(country[0].upper(), city_ids)

            if city_ids and alternames:
                print("FOUND", country, city_ids[:5], [item['id'] for item in alternames][:5])
            else:
                print("NOT FOUND", country, city_ids[:5], [item['id'] for item in alternames][:5])

            for altername in alternames:

                columns = ', '.join(altername.keys())

                placeholders = ':' + ', :'.join(altername.keys())

                query = 'INSERT OR IGNORE INTO alternames (%s) VALUES (%s)' % (columns, placeholders)

                cursor.execute(query, altername)


        cities = cursor.execute(f"select * from cities").fetchall()

        for city in cities:
            alternames = cursor.execute(f"select * from alternate where geonameid == '{city[0]}'").fetchall()
            if len(alternames) > 1:
                print("FOUND", city, alternames)
            if not alternames:
                print("NOT FOUND", city, alternames)

        cls.connection.commit()

        with open(f'alternateNamesV2.csv', 'r') as file:
            reader = csv.DictReader(file)
            field = reader.fieldnames
            for row in reader:

                columns = ', '.join([key for key in row.keys() if key is not None])

                placeholders = ':' + ', :'.join([key for key in row.keys() if key is not None])

                query = 'INSERT OR IGNORE INTO alternate (%s) VALUES (%s)' % (columns, placeholders)

                cursor.execute(query, row)

        cls.connection.commit()

        with open(f"alternateNamesV2.txt", 'r') as file:
            reader = csv.reader(file, delimiter='\t')
            rows = list(reader)

            with open(f'alternateNamesV2.csv', 'w') as file:
                writer = csv.writer(file)
                writer.writerow(
                    (
                        "alternateNameId",
                        "geonameid",
                        "isolanguage",
                        "alternate_name",
                        "isPreferredName",
                        "isShortName",
                        "isColloquial",
                        "isHistoric",
                    )
                )
                writer.writerows(rows)

from OSMPythonTools.overpass import Overpass
    overpass = Overpass()
    result = overpass.query(
        """
        [out:json];
        area["ISO3166-1"="RU"];
        node ["place"="Chelyabinsk"](area);
        out;
        """
    )
    stephansdom = result.elements()[0]
    print(stephansdom)

    import overpass
    api = overpass.API("http://overpass-api.en/api/interpreter")
    response = api.get('node["name:en"="Chelyabinsk"]')
    print(response)

if __name__ == "__main__":
    Collector.processing()

