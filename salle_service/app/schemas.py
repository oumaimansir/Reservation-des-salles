from pydantic import BaseModel

class SalleCreate(BaseModel):
    nom: str
    capacite: int

    class Config:
        orm_mode = True

class Salle(BaseModel):
    id: int
    nom: str
    capacite: int

    class Config:
        orm_mode = True
