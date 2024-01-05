import sqlite3

from typing import Any
from settings import Settings


def get_connection() -> sqlite3.Connection:
    connection = sqlite3.connect(Settings.SQLITE_DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def get_cursor(connection: sqlite3.Connection) -> sqlite3.Cursor:
    return connection.cursor()


class _CRUD:
    table: str = None
    keys: list[str] = None

    @classmethod
    def init(cls, cursor: sqlite3.Cursor) -> None:
        print(f"[CRUD] Init table:{cls.table}")
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS {table}({keys})".format(
                table=cls.table,
                keys=", ".join(cls.keys)
            )
        )

    @classmethod
    def add(cls, cursor: sqlite3.Cursor, row: dict) -> None:
        columns = ', '.join(row.keys())

        placeholders = ':' + ', :'.join(row.keys())

        query = 'INSERT OR IGNORE INTO %s (%s) VALUES (%s)' % (cls.table, columns, placeholders)

        cursor.execute(query, row)

        print(f"[CRUD] {cls.table} add row: {row}")

    @classmethod
    def update(cls, cursor: sqlite3.Cursor, key: str, value: Any, **updated_fields) -> None:
        fields = ", ".join([f'{key}="{value}"' for key, value in updated_fields.items()])

        query = f'UPDATE {cls.table} SET {fields} WHERE {key} == {value}'

        cursor.execute(query)

    @classmethod
    def get_list(cls, cursor: sqlite3.Cursor, query: str) -> list[dict]:
        rows = cursor.execute(query).fetchall()
        return [dict(row) for row in rows]

    @classmethod
    def exist(cls, cursor: sqlite3.Cursor) -> bool:
        query = f"select EXISTS(select * from {cls.table} limit 1)"

        result = cursor.execute(query).fetchone()

        print(f"[CRUD] {cls.table} is exists: {True if result[0] else False}")

        return True if result[0] else False


class GeonamesCityCRUD(_CRUD):
    table: str = Settings.SQLITE_GEONAMES_CITY_TABLE
    keys: list[str] = Settings.SQLITE_GEONAMES_CITY_KEYS

    @classmethod
    def get_list_country_id(cls, cursor: sqlite3.Cursor) -> list[dict]:
        query = f"select country_id from {cls.table} group by country_id"
        return cls.get_list(cursor, query)

    @classmethod
    def get_list_by_country(cls, cursor: sqlite3.Cursor, country_id: str) -> list[dict]:
        query = f"select * from {cls.table} where country_id == '{country_id}'"
        return cls.get_list(cursor, query)


class GeonamesAlternateCRUD(_CRUD):
    table: str = Settings.SQLITE_GEONAMES_ALTER_TABLE
    keys: list[str] = Settings.SQLITE_GEONAMES_ALTER_KEYS

    @classmethod
    def get_list_by_city(cls, cursor: sqlite3.Cursor, city_id: int) -> list[dict]:
        query = f"select * from {cls.table} where city_id == {city_id}"
        return cls.get_list(cursor, query)


class CityCRUD(_CRUD):
    table: str = Settings.SQLITE_CITY_TABLE
    keys: list[str] = Settings.SQLITE_CITY_KEYS

    @classmethod
    def get_list_without_translation(cls, cursor: sqlite3.Cursor) -> list[dict]:
        filters = " or ".join([f"{language} is null" for language in Settings.AVAILABLE_LANGUAGES])

        query = f"select * from {cls.table} where ({filters})"

        return cls.get_list(cursor, query)

    @classmethod
    def get_list_by_country(cls, cursor: sqlite3.Cursor, country_id: str) -> list[dict]:
        query = f"select * from {cls.table} where country_id == '{country_id}'"
        return cls.get_list(cursor, query)


class CountryCRUD(_CRUD):
    table: str = Settings.SQLITE_COUNTRY_TABLE
    keys: list[str] = Settings.SQLITE_COUNTRY_KEYS


class LanguageCRUD(_CRUD):
    table: str = Settings.SQLITE_LANGUAGE_TABLE
    keys: list[str] = Settings.SQLITE_LANGUAGE_KEYS
