from quart import Blueprint, render_template
from database.database import AsyncSessionLocal
from models.categoria import Categoria
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload

nueva_categoria_bp = Blueprint('nueva_categoria', __name__)

@nueva_categoria_bp.route('/')
async def nueva_categoria():
    async with AsyncSessionLocal() as session:
        result = await session.execute(
            select(Categoria).options(selectinload(Categoria.productos))
        )
        categorias = result.scalars().all()

    return await render_template('modal-nueva-categoria.html', categorias=categorias)