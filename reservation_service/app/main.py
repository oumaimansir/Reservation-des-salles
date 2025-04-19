from fastapi import FastAPI
from app import models, database, routes
from kafka import KafkaConsumer
import threading
import json

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.include_router(routes.router)
def listen_to_auth_topic():
    consumer = KafkaConsumer(
        'auth-topic',
        bootstrap_servers='localhost:9092',
        group_id='reservation-group',
        value_deserializer=lambda m: json.loads(m.decode('utf-8'))
    )

    for message in consumer:
        data = message.value
        print("📨 Message reçu dans reservation_service:", data)
        # Tu peux ici déclencher une action, ex: enregistrer une log, notifier, etc.

# Démarrer le consumer dans un thread séparé pour ne pas bloquer FastAPI
threading.Thread(target=listen_to_auth_topic, daemon=True).start()

@app.get("/")
def home():
    return {"message": "Reservation service fonctionne avec Kafka"}
