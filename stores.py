import json

from settings import Settings
from utils import jsonf
from utils import string_to_list


class _Store:
    dir = f"{Settings.STATIC_DIR}/{Settings.STORE_DIR}"

    filename: str = None

    @classmethod
    def read(cls) -> list[dict]:
        with open(f"{cls.dir}/{jsonf(cls.filename)}", "r") as file:
            return json.loads(file.read())


class StoreCountry(_Store):
    filename: str = "countries"

    @classmethod
    def get(cls) -> list[dict]:
        return [
            dict(
                id=country["Country code"],
                name=country["Country name"],
                languages=list(
                    set(
                        string_to_list(country["iOS languages"])
                        + string_to_list(country["Android languages"])
                    )
                ),
            )
            for country in cls.read()
        ]


class StoreLanguage(_Store):
    filename: str = "languages"

    @classmethod
    def get(cls) -> list[dict]:
        return [
            dict(
                id=language["Language code "],
                name=language["Language name "],
                origin=None,
            )
            for language in cls.read()
        ]
