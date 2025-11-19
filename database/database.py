from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from contextlib import asynccontextmanager

# --- Configuración de SQLite ---
DATABASE_URL = "sqlite+aiosqlite:///./ecomdata.db"

engine = create_async_engine(DATABASE_URL, echo=True, future=True)

AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

Base = declarative_base()


# -- Función get_db() para usar en rutas ---
@asynccontextmanager
async def get_db():
    """Provee una sesión de base de datos asíncrona para usar en rutas."""
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()