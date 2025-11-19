from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from database.database import Base


class Categoria(Base):
    __tablename__ = "categorias"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False, unique=True)
    descripcion = Column(Text, nullable=True)

    # Relación hacia Producto (carga en selectin por defecto en consultas si se usa options)
    productos = relationship("Producto", back_populates="categoria", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Categoria(nombre={self.nombre})>"