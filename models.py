from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
import datetime


class Finance(Base):
    __tablename__ = 'finance'
    id = Column(Integer, primary_key=True, index=True)
    operation = Column(String)
    money = Column(Integer)
    date = datetime.date.today()
    user_id = Column(Integer, ForeignKey('users.id'))


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    money = Column(Integer)
    password = Column(String)