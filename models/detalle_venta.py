from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from database.database import Base

class DetalleVenta(Base):
    __tablename__ = "detalle_ventas"

    id = Column(Integer, primary_key=True, index=True)
    venta_id = Column(Integer, ForeignKey("ventas.id"), nullable=False)
    producto_id = Column(Integer, ForeignKey("productos.id"), nullable=False)
    cantidad = Column(Integer, nullable=False)
    precio_unitario = Column(Float, nullable=False)
    subtotal = Column(Float, nullable=False)

    venta = relationship("Venta", back_populates="detalles")
    producto = relationship("Producto")

    def __repr__(self):
        return f"<DetalleVenta(venta_id={self.venta_id}, producto_id={self.producto_id}, cantidad={self.cantidad})>"
