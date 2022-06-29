from sqlalchemy.orm import sessionmaker, Session
from models import Base, User, Profile, Address
from utils import setup_db_engine, create_database_if_not_exists


def create_user(
        session: Session, email: str, password: str, phone: str, age: int, city: str, address: str
) -> User:
    user = User(email=email, password=password)
    profile = Profile(user=user, phone=phone, age=age)
    address = Address(user=user, city=city, address=address)

    session.add_all((user, profile, address))
    session.commit()

    return user


def update_or_create(session: Session, user: str, city: str, address: str) -> Address:
    if len(user.addresses):
        current_address = user.addresses[0]
        current_address = city
        current_address = address
    else:
        current_address = Address(user=user, city=city, address=address)

    session.add(address)
    session.commit()

    return address


if __name__ == "__main__":
    engine = setup_db_engine()
    create_database_if_not_exists(engine=engine)

    Base.metadata.create_all(engine)
    CurrentSession = sessionmaker(bind=engine)
    current_session = CurrentSession()

    new_user = create_user(
        session=current_session,
        email='test@test.by',
        password='test',
        phone='+322321512',
        age='26',
        city='Minsk',
        address="Address12134",
    )