from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from database.database import Base

class Inventario(Base):
    __tablename__ = "inventario"

    id = Column(Integer, primary_key=True, index=True)
    producto_id = Column(Integer, ForeignKey("productos.id"), nullable=False)
    cantidad = Column(Integer, nullable=False)
    fecha_actualizacion = Column(DateTime, default=datetime.utcnow)

    producto = relationship("Producto", backref="movimientos_inventario")

    def __repr__(self):
        return f"<Inventario(producto_id={self.producto_id}, cantidad={self.cantidad})>"