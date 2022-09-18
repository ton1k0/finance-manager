import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base
from sqlalchemy.sql import func



class Finance(Base):
    __tablename__ = 'finance'
    id = Column(Integer, primary_key=True, index=True)
    operation = Column(String)
    money = Column(Integer)
    create_date = Column(DateTime, default=func.now())
    user_id = Column(Integer, ForeignKey('users.id'))

    creator = relationship("User", back_populates="finances")

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    money = Column(Integer)
    password = Column(String)

    finances = relationship('Finance', back_populates='creator')