import sqlite3


def select_username(name: str):
    with sqlite3.connect("my_database.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
               SELECT *
               FROM user
               WHERE firstname = ?;
               """,
            (name,)
        )
        session.commit()
        return cursor.fetchall()


def select_age(age: int):
    with sqlite3.connect("my_database.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            SELECT *
            FROM user
            WHERE age = ?;
            """,
            (age,)
        )
        session.commit()
        return cursor.fetchall()


def search(name_or_age):
    if type(name_or_age) == int:
        age = name_or_age
        return select_age(age)
    if type(name_or_age) == str:
        name = name_or_age
        return select_username(name)


if __name__ == "__main__":
    print(search(12))
    print(search("STT3"))
