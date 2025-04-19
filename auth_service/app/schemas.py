from pydantic import BaseModel
from enum import Enum

class RoleEnum(str, Enum):
    admin = "admin"
    employe = "employe"
    visiteur = "visiteur"

class UserCreate(BaseModel):
    email: str
    password: str
    role: RoleEnum = RoleEnum.visiteur
class UserOut(BaseModel):
    id: int
    email: str
    role: RoleEnum
    class Config:
        orm_mode = True

class RegisterResponse(BaseModel):
    message: str
    user: UserOut

class Token(BaseModel):
    access_token: str
    token_type: str
