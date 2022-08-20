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
    name:str
    money: int
    class Config():
        orm_mode=True