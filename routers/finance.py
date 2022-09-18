from fastapi import APIRouter, Depends, status
import schemas, oaut2
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from scripts import finance



router = APIRouter(
    prefix='/finance',
    tags=['finance']
)

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Finance,db: Session = Depends(get_db), current_user:schemas.User_id = Depends(oaut2.get_current_user)):
    return finance.create(request,current_user, db)

@router.get('/', status_code=status.HTTP_202_ACCEPTED, response_model=List[schemas.ShowFinance])
def all(db:Session = Depends(get_db)):
    return finance.get_all(db)


@router.get('/history/all', response_model= List[schemas.Operation])
def get_user_history(db:Session = Depends(get_db),current_user:schemas.User_id = Depends(oaut2.get_current_user)):
    return finance.get_all_user_history(db,current_user)


@router.get('/history/month', response_model= schemas.Operations)
def get_user_month_history(db:Session = Depends(get_db), current_user:schemas.User_id = Depends(oaut2.get_current_user)):
    return  finance.get_user_month_history(db,current_user)