from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas, database

app = FastAPI()

# Dépendance pour obtenir la session DB
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Route pour ajouter une salle
@app.post("/salles/")
def ajouter_salle(salle: schemas.SalleCreate, db: Session = Depends(get_db)):
    return crud.ajouter_salle(db, salle)

# Route pour supprimer une salle
@app.delete("/salles/{salle_id}")
def supprimer_salle(salle_id: int, db: Session = Depends(get_db)):
    salle = crud.supprimer_salle(db, salle_id)
    if salle is None:
        raise HTTPException(status_code=404, detail="Salle non trouvée")
    return {"message": "Salle supprimée avec succès"}

# Route pour obtenir toutes les salles
@app.get("/salles/")
def get_salles(db: Session = Depends(get_db)):
    return crud.get_salles(db)
