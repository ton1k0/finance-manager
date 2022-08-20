from sqlalchemy.orm import Session
import models, schemas



def create(request: schemas.Finance, db: Session):
    new_operation = models.Finance(operation=request.operation, money=request.money, date=request.date)
    db.add(new_operation)
    db.commit()
    db.refresh(new_operation)
    return new_operation