from sqlalchemy import Column, Integer, String, DateTime, Boolean
from datetime import datetime
from database.database import Base

class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(120), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    telefono = Column(String(50), nullable=True)
    direccion = Column(String(255), nullable=True)
    activo = Column(Boolean, default=True)
    fecha_registro = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Cliente(nombre={self.nombre}, email={self.email})>"
