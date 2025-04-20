from fastapi import FastAPI
from app import models, database
from .routes import router
from app.schemas import RegisterResponse, UserOut
from sqlalchemy.orm import Session
from app.database import get_db  # ou l'import correct selon ton projet
from fastapi import Depends
from app.schemas import UserCreate
from fastapi import HTTPException
from app.models import User
from app.database import SessionLocal
from app.utils import hash_password, verify_password  
models.Base.metadata.create_all(bind=database.engine)
from kafka import KafkaProducer
import json
app = FastAPI()
producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

@app.post("/register", response_model=RegisterResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    # Vérifier si l'email existe déjà
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Hacher le mot de passe
    hashed_password = hash_password(user.password)
    
    # Créer un nouvel utilisateur
    new_user = User(email=user.email, hashed_password=hashed_password, role=user.role)
    
    # Ajouter l'utilisateur à la base de données
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    producer.send('auth-topic', {'event': 'user_registered', 'user': user.dict()})

    producer.flush()
    
    return {"message": "Utilisateur enregistré et message envoyé à Kafka", "user": new_user}
@app.post("/login")
def login(user: UserCreate, db: Session = Depends(get_db)):
    # Rechercher l'utilisateur par email
    db_user = db.query(User).filter(User.email == user.email).first()
    
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    return {"message": "Login successful", "username": db_user.email}
