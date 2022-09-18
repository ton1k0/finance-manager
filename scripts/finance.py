from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from sqlalchemy import desc
import models, schemas



def create(request: schemas.Finance,current_user: schemas.User_id, db: Session):
    new_operation = models.Finance(operation=request.operation, money=request.money, user_id= current_user.id)
    db_user = db.query(models.User).filter(models.User.id == current_user.id).first()
    if str(request.operation) == '+':
        db_user.money += request.money
    if str(request.operation) == '-':
        db_user.money -= request.money
    db.add(new_operation)
    db.commit()
    db.refresh(new_operation)
    return new_operation

def get_all(db: Session):
    operations = db.query(models.Finance).all()
    return operations


def get_all_user_history(db: Session,current_user: schemas.User_id):
    user_operations = db.query(models.Finance).filter(models.Finance.user_id == current_user.id).all()
    return user_operations


def get_user_month_history(db: Session, current_user: schemas.User_id):
    now = datetime.now()
    one_month_ago = now - timedelta(days=30)
    operations = db.query(models.Finance).filter(models.Finance.user_id == current_user.id,
                                                            models.Finance.create_date >= one_month_ago).all()
    stonks = 0
    expenses = 0
    for operation in operations:
        if operation.operation == '+':
            stonks += operation.money
        elif operation.operation == '-':
            expenses -= operation.money
    return {
        'operations': operations,
        'stonks': stonks,
        'expenses': expenses
    }