import json

from settings import Settings
from utils import jsonf


class _Github:
    dir = f"{Settings.STATIC_DIR}/{Settings.GITHUB_DIR}"

    filename: str = None

    @classmethod
    def read(cls) -> list[dict]:
        with open(f"{cls.dir}/{jsonf(cls.filename)}", "r") as file:
            return json.loads(file.read())


class GitHubCountry(_Github):
    filename: str = "countries"

    @classmethod
    def get(cls) -> list[dict]:
        return [
            dict(
                id=country["country_code_name"],
                name=country["country_name"],
                languages=[country["lang_code"]] if country.get("lang_code") else [],
            )
            for country in cls.read()
        ]


class GitHubLanguage(_Github):
    filename: str = "languages"

    @classmethod
    def get(cls) -> list[dict]:
        return [
            dict(
                id=language["code"],
                name=language["name"],
                origin=language["nativeName"],
            )
            for language in cls.read()
        ]
