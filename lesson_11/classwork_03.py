import sqlite3

def create_user():
    with sqlite3.connect("my_database.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            CREATE TABLE user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            firstname text,
            lastname text,
            email text,
            password TEXT,
            age INTEGER
            )"""
        )
        session.commit()

create_user()