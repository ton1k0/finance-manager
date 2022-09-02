from typing import Optional

from pydantic import BaseModel
from datetime import date

class FinanceBase(BaseModel):
    operation: str
    money: int
    date: date


class Finance(FinanceBase):
    class Config():
        orm_mode=True


class User(BaseModel):
    name: str
    money: int
    password: str


class ShowUser(BaseModel):
    id: int
    name: str
    class Config():
        orm_mode=True

class User_id(BaseModel):
    id: int

class ShowFinance(BaseModel):
    operation: str
    money: int
    date: date
    class Config():
        orm_mode=True

class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    name: Optional[str] = None