from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)

    addresses = relationship("Address", back_populates="user")
    profile = relationship("Profile", back_populates="user")


class Address(Base):
    __tablename__ = "addresses"
    id = Column(Integer, primary_key=True)
    city = Column(String)
    house = Column(String)

    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="addresses")


class Profile(Base):
    __tablename__ = "profile"
    id = Column(Integer, primary_key=True)
    age = Column(Integer)
    phone = Column(String)

    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="profile")

