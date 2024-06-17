from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from src.infrastructure.database.config.base import Base
import uuid
class Grimoire(Base):
    __tablename__ = 'grimoires'
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    nombre = Column(String(50), nullable=False)
    nivel = Column(Integer, nullable=False)

