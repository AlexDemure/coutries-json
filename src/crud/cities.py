from sqlite3 import Cursor

from src.core.settings import Settings

from .base import CRUD
from .base import get_list


class CityCRUD(CRUD):
    table: str = Settings.SQLITE_CITY_TABLE
    keys: list[str] = Settings.SQLITE_CITY_KEYS

    @classmethod
    def get_list_without_translation(cls, cursor: Cursor) -> list[dict]:
        filters = " or ".join(
            [f"{language} is null" for language in Settings.AVAILABLE_LANGUAGES]
        )

        query = f"select * from {cls.table} where ({filters})"

        return get_list(cursor, query)

    @classmethod
    def get_list_by_country(cls, cursor: Cursor, country_id: str) -> list[dict]:
        query = f"select * from {cls.table} where country_id == '{country_id}'"
        return get_list(cursor, query)
