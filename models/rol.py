from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database.database import Base

class Rol(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), unique=True, nullable=False)
    descripcion = Column(String(200), nullable=True)

    # Relación bidireccional con Usuario
    usuarios = relationship('Usuario', back_populates='rol')

    def __repr__(self):
        return f"<Rol(nombre={self.nombre})>"