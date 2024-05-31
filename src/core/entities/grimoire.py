from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from src.infrastructure.database.config.base import Base

class Grimoire(Base):
    __tablename__ = 'grimoires'
    
    id = Column(String(36), primary_key=True, default='newid()')
    nombre = Column(String(50), nullable=False)
    nivel = Column(Integer, nullable=False)

