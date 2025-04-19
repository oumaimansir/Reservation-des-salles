from pydantic import BaseModel
from datetime import datetime, time

class ReservationCreate(BaseModel):
    salle_id: int
    user_id: int
    date_reservation: datetime
    heure_debut: time
    heure_fin: time

class Reservation(ReservationCreate):
    id: int

    class Config:
        orm_mode = True
