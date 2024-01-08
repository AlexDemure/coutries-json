from sqlite3 import Cursor
from typing import Any
from typing import Optional


class CRUD:
    table: str = None
    keys: list[str] = None

    @classmethod
    def init(cls, cursor: Cursor) -> None:
        print(f"[CRUD] Init table:{cls.table}")
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS {table}({keys})".format(
                table=cls.table, keys=", ".join(cls.keys)
            )
        )

    @classmethod
    def add(cls, cursor: Cursor, row: dict) -> None:
        columns = ", ".join(row.keys())

        placeholders = ":" + ", :".join(row.keys())

        query = "INSERT OR IGNORE INTO %s (%s) VALUES (%s)" % (
            cls.table,
            columns,
            placeholders,
        )

        cursor.execute(query, row)

        print(f"[CRUD] {cls.table} add row: {row}")

    @classmethod
    def update(cls, cursor: Cursor, key: str, value: Any, **updated_fields) -> None:
        fields = ", ".join(
            [f'{key}="{value}"' for key, value in updated_fields.items()]
        )

        query = f"UPDATE {cls.table} SET {fields} WHERE {key} == {value}"

        cursor.execute(query)

    @classmethod
    def get(cls, cursor: Cursor, key: str, value: Any) -> Optional[dict]:
        query = f"SELECT * from {cls.table} WHERE {key} == '{value}'"

        row = cursor.execute(query).fetchone()

        return dict(row) if row else None

    @classmethod
    def get_by_fields(cls, cursor: Cursor, **kwargs) -> Optional[dict]:
        fields = " and ".join([f'{key}="{value}"' for key, value in kwargs.items()])

        query = f"SELECT * FROM {cls.table} WHERE {fields}"

        row = cursor.execute(query).fetchone()

        return dict(row) if row else None

    @classmethod
    def exist(cls, cursor: Cursor) -> bool:
        query = f"select EXISTS(select * from {cls.table} limit 1)"

        result = cursor.execute(query).fetchone()

        print(f"[CRUD] {cls.table} is exists: {True if result[0] else False}")

        return True if result[0] else False


def get_list(cursor: Cursor, query: str) -> list[dict]:
    rows = cursor.execute(query).fetchall()
    return [dict(row) for row in rows]
