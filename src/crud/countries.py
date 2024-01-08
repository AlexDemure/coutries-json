from sqlite3 import Cursor

from src.core.settings import Settings

from .base import CRUD
from .base import get_list


class CountryCRUD(CRUD):
    table: str = Settings.SQLITE_COUNTRY_TABLE
    keys: list[str] = Settings.SQLITE_COUNTRY_KEYS

    @classmethod
    def get_list_ids(cls, cursor: Cursor) -> list[dict]:
        query = f"select id from {cls.table}"
        return get_list(cursor, query)

    @classmethod
    def get_list(cls, cursor: Cursor) -> list[dict]:
        query = f"select * from {cls.table}"
        return get_list(cursor, query)


class CountryLanguageCRUD(CRUD):
    table: str = Settings.SQLITE_M2M_COUNTRY_LANGUAGE_TABLE
    keys: list[str] = Settings.SQLITE_M2M_COUNTRY_LANGUAGE_KEYS
