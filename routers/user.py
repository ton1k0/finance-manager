from fastapi import APIRouter, Depends
import schemas
from sqlalchemy.orm import Session
from database import get_db
from scripts import user


router = APIRouter(
    prefix='/user',
    tags=['Users']
)

@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create_user(request,db)