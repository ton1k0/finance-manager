from typing import Optional, List
from pydantic import BaseModel
from datetime import date



class FinanceBase(BaseModel):
    operation: str
    money: int


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
    create_date: date
    creator: ShowUser
    class Config():
        orm_mode=True


class Operation(BaseModel):
    operation: str
    money: int
    create_date: date
    class Config():
        orm_mode=True


class Operations(BaseModel):
    operations: List[Operation]
    stonks: int
    expenses: int
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