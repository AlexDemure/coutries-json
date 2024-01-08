import sqlite3

from src.core.settings import Settings


def get_connection() -> sqlite3.Connection:
    connection = sqlite3.connect(Settings.SQLITE_DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def get_cursor(connection: sqlite3.Connection) -> sqlite3.Cursor:
    return connection.cursor()
