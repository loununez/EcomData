from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey, String
from sqlalchemy.orm import relationship
from datetime import datetime
from database.database import Base

class Pago(Base):
    __tablename__ = "pagos"

    id = Column(Integer, primary_key=True, index=True)
    venta_id = Column(Integer, ForeignKey("ventas.id"), nullable=False)
    monto = Column(Float, nullable=False)
    metodo = Column(String(50), nullable=False)
    fecha_pago = Column(DateTime, default=datetime.utcnow)

    venta = relationship("Venta", backref="pagos")

    def __repr__(self):
        return f"<Pago(metodo={self.metodo}, monto={self.monto})>"