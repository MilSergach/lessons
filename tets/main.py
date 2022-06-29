from test1 import create_engine_db, create_db
from sqlalchemy.orm import sessionmaker, Session
from model import User, Base, Profile, Address


def create_new_user(
        session: Session, email: str, password: str, city: str, house: str, age: int, phone: str
) -> User:
    user = User(email=email, password=password)
    address = Address(user=user, city=city, house=house)
    profile = Profile(user=user, age=age, phone=phone)

    session.add_all((user, address, profile))
    session.commit()

    return user

if __name__ == "__main__":
    engine = create_engine_db()
    create_db(engine=engine)

    Base.metadata.create_all(engine)
    CurrentSession = sessionmaker(bind=engine)
    current_session = CurrentSession()

    new_user = create_new_user(
        session=current_session,
        email="1test1@gmail.com",
        password="password1test1",
        city="Minsk",
        house="Avenue1",
        age='12',
        phone="+1298037547",
    )