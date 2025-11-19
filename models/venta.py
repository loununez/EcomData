from sqlalchemy import Column, Integer, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from database.database import Base

class Venta(Base):
    __tablename__ = "ventas"

    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey("clientes.id"), nullable=False)
    fecha = Column(DateTime, default=datetime.utcnow)
    total = Column(Float, nullable=False)

    cliente = relationship("Cliente", backref="ventas")
    detalles = relationship("DetalleVenta", back_populates="venta")

    def __repr__(self):
        return f"<Venta(id={self.id}, total={self.total})>" 