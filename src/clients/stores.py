import json

from src.core.settings import Settings
from src.utils import jsonf
from src.utils import string_to_list


class _StoreClient:
    dir = f"{Settings.STATIC_DIR}/{Settings.STORE_DIR}"

    filename: str = None

    @classmethod
    def read(cls) -> list[dict]:
        with open(f"{cls.dir}/{jsonf(cls.filename)}", "r") as file:
            return json.loads(file.read())


class StoreCountry(_StoreClient):
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


class StoreLanguage(_StoreClient):
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
