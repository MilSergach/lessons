import sqlite3

def create_user(firstname: str, lastname: str, email: str, password: str, age: int):
    with sqlite3.connect("my_database.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            INSERT INTO user (firstname, lastname, email, password, age)
            VALUES (?, ?, ?, ?, ?);
            """,
            (firstname, lastname, email, password, age),
        )
        session.commit()

if __name__ == "__main__":
    create_user("Serg","Mil","Serg.mil@m.com", "91230123", 12)
    create_user("Test", "Mil", "Test.mil@m.com", "Test0123", 22)
    create_user("Serg", "Test", "Serg.test@m.com", "9test4123", 32)
    create_user("Serg", "1234", "Serg1234@m.com", "91asdgasdg0123", 46)
    create_user("STT3", "M1T", "STT3.M1T@m.com", "9123012sdfg", 20)