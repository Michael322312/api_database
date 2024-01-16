from sqlalchemy import Column, Integer, String
from .engine import Base

class DBUser(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)

