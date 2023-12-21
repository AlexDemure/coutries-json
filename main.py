import json
from typing import Optional


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


def processing() -> list[dict]:

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

        prepared_countries.append(prepared_country)

    with open("result.json", "w") as file:
        file.write(json.dumps(prepared_countries, ensure_ascii=False))


if __name__ == "__main__":
    processing()

