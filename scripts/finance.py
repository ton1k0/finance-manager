from sqlalchemy.orm import Session
import models, schemas



def create(request: schemas.Finance,current_user: schemas.User_id, db: Session):
    new_operation = models.Finance(operation=request.operation, money=request.money, date=request.date, user_id= current_user.id)
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