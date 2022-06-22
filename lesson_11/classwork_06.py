import sqlite3


def search_in_range_years(x: int, y: int):
    with sqlite3.connect("my_database.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            SELECT *
            FROM user
            WHERE age >= ? AND age <= ?
            LIMIT 2, 3;
            """,
            (x, y)
        )
        session.commit()
        return cursor.fetchall()

if __name__ == "__main__":
    print(search_in_range_years(12, 50))
