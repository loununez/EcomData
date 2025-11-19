from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey
from sqlalchemy.orm import relationship
from database.database import Base

class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(150), nullable=False)
    descripcion = Column(Text, nullable=True)
    precio = Column(Float, nullable=False)
    stock = Column(Integer, default=0)

    categoria_id = Column(Integer, ForeignKey("categorias.id"), nullable=False)
    categoria = relationship("Categoria", back_populates="productos")

    def __repr__(self):
        return f"<Producto(nombre={self.nombre}, precio={self.precio})>"