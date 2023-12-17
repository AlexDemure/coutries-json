import json


def generate() -> None:
    with open("countries_with_languages.json", "r") as file:
        countries_with_languages: list[dict] = json.loads(file.read())

    with open("world_countries.json", "r") as file:
        world_countries: list[dict] = json.loads(file.read())

    with open("languages.json", "r") as file:
        languages: list[dict] = json.loads(file.read())

    prepared_countries = []

    for country_item in countries_with_languages:

        language = None
        if country_item.get('lang_code'):
            language = [x for x in languages if x['code'].lower() == country_item['lang_code'].lower()]
            if language:
                language = language[0]

        country = None
        if country_item.get("country_code_name"):
            country = [x for x in world_countries if x['alpha2'].lower() == country_item['country_code_name'].lower()]
            if country:
                country = country[0]

        if not country and language:
            print(country_item)
            continue

        prepared_countries.append(
            dict(
               country_iso=country['id'] if country else None,
               country_code=country['alpha2'] if country else None,
               country_en=country['en'] if country else None,
               country_ru=country['ru'] if country else None,
               language_code=language['code'] if language else None,
               language_native=language['nativeName'] if language else None
            )
        )

    with open("countries.json", "w") as file:
        file.write(json.dumps(prepared_countries, ensure_ascii=False))


if __name__ == "__main__":
    generate()

