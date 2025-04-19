from sqlalchemy import Column, Integer, String
from .database import Base
from sqlalchemy import Enum as SqlEnum
import enum

class RoleEnum(enum.Enum):
    admin = "admin"
    employe = "employe"
    visiteur = "visiteur"
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(SqlEnum(RoleEnum), default=RoleEnum.visiteur)
