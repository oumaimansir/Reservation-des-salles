from sqlalchemy.orm import Session
from . import models, schemas

# Ajouter une salle
def ajouter_salle(db: Session, salle: schemas.SalleCreate):
    db_salle = models.Salle(nom=salle.nom, capacite=salle.capacite)
    db.add(db_salle)
    db.commit()
    db.refresh(db_salle)
    return db_salle

# Supprimer une salle
def supprimer_salle(db: Session, salle_id: int):
    salle = db.query(models.Salle).filter(models.Salle.id == salle_id).first()
    if salle:
        db.delete(salle)
        db.commit()
    return salle

# Obtenir toutes les salles
def get_salles(db: Session):
    return db.query(models.Salle).all()
