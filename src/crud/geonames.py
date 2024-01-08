from sqlite3 import Cursor

from src.core.settings import Settings

from .base import CRUD
from .base import get_list


class GeonamesCityCRUD(CRUD):
    table: str = Settings.SQLITE_GEONAMES_CITY_TABLE
    keys: list[str] = Settings.SQLITE_GEONAMES_CITY_KEYS

    @classmethod
    def get_list_country_id(cls, cursor: Cursor) -> list[dict]:
        query = f"select country_id from {cls.table} group by country_id"
        return get_list(cursor, query)

    @classmethod
    def get_list_by_country(cls, cursor: Cursor, country_id: str) -> list[dict]:
        query = f"select * from {cls.table} where country_id == '{country_id}'"
        return get_list(cursor, query)


class GeonamesAlternateCRUD(CRUD):
    table: str = Settings.SQLITE_GEONAMES_ALTER_TABLE
    keys: list[str] = Settings.SQLITE_GEONAMES_ALTER_KEYS

    @classmethod
    def get_list_by_city(cls, cursor: Cursor, city_id: int) -> list[dict]:
        query = f"select * from {cls.table} where city_id == {city_id}"
        return get_list(cursor, query)
