from fastapi import Depends
import schemas, models
from sqlalchemy.orm import Session
from database import get_db


def create_user(request: schemas.User, db: Session = Depends(get_db)):
    new_user = models.User(name=request.name,money=request.money, password=request.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user