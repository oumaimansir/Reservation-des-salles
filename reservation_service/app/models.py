from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Time
from .database import Base
from datetime import datetime, time

class Reservation(Base):
    __tablename__ = "reservations"

    id = Column(Integer, primary_key=True, index=True)
    salle_id = Column(Integer)
    user_id = Column(Integer)
    date_reservation = Column(DateTime, default=datetime.utcnow)
    heure_debut = Column(Time, default=time(9, 0))
    heure_fin = Column(Time, default=time(17, 0))
