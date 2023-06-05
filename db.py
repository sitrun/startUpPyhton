import os
from typing import Dict, List, Tuple

import sqlite3

# Подключаем базу данных бота
conn = sqlite3.connect("db_breathe.db")
cursor = conn.cursor()


def insert(table: str, column_values: Dict):
    columns = ', '.join(column_values.keys())
    values = [tuple(column_values.values())]
    placeholders = ", ".join("?" * len(column_values.keys()))
    cursor.executemany(
        f"INSERT INTO {table} "
        f"({columns}) "
        f"VALUES ({placeholders})",
        values)
    conn.commit()
    # Получить последний индекс
    cursor.execute(f"SELECT MAX(id) FROM {table}")
    last_id = cursor.fetchone()
    return last_id[0]

    # Пример работы функции
    # clist = [("abc",), ("def",), ("ghi",)]
    # cursor.executemany("INSERT INTO myTable(data) values(?)", clist)


def update(table: str, column_values: Dict, where: str = ""):
    set_colums = []
    for column, value in column_values.items():
        value_in = f"'{value}'" if isinstance(value, str) else int(value)
        set_colums.append(f"{column} = {value_in}")

    set_colums_db = ', '.join(set_colums)
    sql = f"UPDATE {table} SET {set_colums_db} WHERE {where}"
    cursor.execute(sql)
    conn.commit()


def fetchall(table: str, columns: List[str]) -> List[Tuple]:
    columns_joined = ", ".join(columns)
    cursor.execute(f"SELECT {columns_joined} FROM {table}")
    rows = cursor.fetchall()
    result = []
    for row in rows:
        dict_row = {}
        for index, column in enumerate(columns):
            dict_row[column] = row[index]
        result.append(dict_row)
    return result


def fetch_where(table: str, columns: List[str], where_str: str) -> List[Tuple]:
    columns_joined = ", ".join(columns)
    cursor.execute(f"SELECT {columns_joined} FROM {table} WHERE {where_str}")
    rows = cursor.fetchall()
    result = []
    for row in rows:
        dict_row = {}
        for index, column in enumerate(columns):
            dict_row[column] = row[index]
        result.append(dict_row)
    return result


def delete(table: str, row_id: int, where: str = '') -> None:
    row_id = int(row_id)
    if where:
        cursor.execute(f"delete from {table} where {where}")
    else:
        cursor.execute(f"delete from {table} where id={row_id}")
        conn.commit()


def get_cursor():
    return cursor


def _init_db():
    """Инициализирует БД"""
    with open("setup.sql", "r") as f:
        sql = f.read()
    cursor.executescript(sql)
    conn.commit()


def check_db_exists():
    """Проверяет, инициализирована ли БД, если нет — инициализирует"""
    cursor.execute("SELECT name FROM sqlite_master "
                   "WHERE type='table' AND name='breezes'")
    table_exists = cursor.fetchall()
    if table_exists:
        return
    _init_db()


check_db_exists()
