from sqlalchemy import Column, Integer, String, Boolean
from database.database import Base

class ConfiguracionGeneral(Base):
    __tablename__ = "configuracion_general"

    id = Column(Integer, primary_key=True, index=True)
    nombre_empresa = Column(String(150), nullable=False)
    direccion = Column(String(255), nullable=True)
    telefono = Column(String(50), nullable=True)
    email_contacto = Column(String(120), nullable=True)

class ConfiguracionNotificacion(Base):
    __tablename__ = "configuracion_notificaciones"

    id = Column(Integer, primary_key=True, index=True)
    email_notificaciones = Column(String(120), nullable=False)
    notificar_ventas = Column(Boolean, default=True)
    notificar_stock = Column(Boolean, default=True)

class ConfiguracionSeguridad(Base):
    __tablename__ = "configuracion_seguridad"

    id = Column(Integer, primary_key=True, index=True)
    politica_password = Column(String(200), nullable=True)
    doble_factor = Column(Boolean, default=False)
