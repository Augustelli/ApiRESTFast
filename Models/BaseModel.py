from sqlalchemy import Column, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class BaseModel(Base):
    __tablename__ = 'basemodel'
    id = Column(Integer, primary_key=True, index=True)