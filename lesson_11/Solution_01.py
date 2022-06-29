import sqlite3


def create_products():
    with sqlite3.connect("products") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            CREATE TABLE products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name text,
            cost INTEGER,
            amount INTEGER,
            comments TEXT
            )"""
        )
        session.commit()


def add_product(name: str, cost: int, amount: int, comments: str):
    with sqlite3.connect("products") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            INSERT INTO products (name, cost, amount, comments)
            VALUES (?, ?, ?, ?);
            """,
            (name, cost, amount, comments),
        )
        session.commit()


def read_all():
    with sqlite3.connect("products") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            SELECT *
            FROM products
            """,
        )
        session.commit()
        print(cursor.fetchall())


def update(products: str, product_id: int, name: str, cost: int, amount: int, comments: str):
    with sqlite3.connect("products") as session:
        cursor = session.cursor()
        cursor.execute(
            """
               UPDATE products
               SET name = ?, cost = ?, amount = ?, comments = ?
               WHERE id = ?;
               
               """,
            (name, cost, amount, comments, product_id)
        )
        session.commit()
        return cursor.fetchall()


def delete():
    pass


if __name__ == "__main__":
    add_product("ttx", 5, 7, 'rawl')
    add_product("rtq", 30, 5, '2r2a2')
