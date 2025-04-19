from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, database

router = APIRouter()

@router.post("/reservations/", response_model=schemas.Reservation)
def create_reservation(res: schemas.ReservationCreate, db: Session = Depends(database.get_db)):
    db_res = models.Reservation(**res.dict())
    db.add(db_res)
    db.commit()
    db.refresh(db_res)
    return db_res
