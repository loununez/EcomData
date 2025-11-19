from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from database.database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    activo = Column(Boolean, default=True)
    fecha_creacion = Column(DateTime, default=datetime.utcnow)

    rol_id = Column(Integer, ForeignKey("roles.id"), nullable=False)
    rol = relationship("Rol")

    def __repr__(self):
        return f"<Usuario(nombre={self.nombre}, email={self.email})>"