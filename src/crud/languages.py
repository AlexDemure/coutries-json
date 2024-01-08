from sqlite3 import Cursor

from src.core.settings import Settings

from .base import CRUD
from .base import get_list


class LanguageCRUD(CRUD):
    table: str = Settings.SQLITE_LANGUAGE_TABLE
    keys: list[str] = Settings.SQLITE_LANGUAGE_KEYS

    @classmethod
    def get_list_by_country(cls, cursor: Cursor, country_id: str) -> list[dict]:
        m2m_table = Settings.SQLITE_M2M_COUNTRY_LANGUAGE_TABLE

        keys = ", ".join([f"{cls.table}.{key}" for key in cls.keys])

        query = f"""
        select {keys} from {cls.table}
        join {m2m_table} on {cls.table}.id = {m2m_table}.language_id
        where {m2m_table}.country_id == '{country_id}'
        """

        return get_list(cursor, query)
