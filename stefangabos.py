import json

from settings import Settings
from utils import jsonf


class StefangabosCountry:
    dir = f"{Settings.STATIC_DIR}/{Settings.STEFANGABOS_DIR}"

    filename: str = "countries"

    @classmethod
    def read(cls) -> list[dict]:
        with open(f"{cls.dir}/{jsonf(cls.filename)}", "r") as file:
            return json.loads(file.read())

    @classmethod
    def get(cls) -> list[dict]:
        return [
            dict(
                id=country["alpha2"],
                **{
                    language: country[language].capitalize()
                    for language in Settings.AVAILABLE_LANGUAGES
                },
            )
            for country in cls.read()
        ]
