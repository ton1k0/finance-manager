from fastapi import APIRouter, Depends, status
import schemas
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from scripts import finance



router = APIRouter(
    prefix='/finance',
    tags=['finance']
)

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Finance, db: Session = Depends(get_db)):
    return finance.create(request,db)