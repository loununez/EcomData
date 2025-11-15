from quart import Blueprint, render_template, request, redirect, url_for, jsonify
from database.database import AsyncSessionLocal
from models.categoria import Categoria
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload

catalogo_categorias_bp = Blueprint('catalogo_categorias', __name__)

@catalogo_categorias_bp.route('/', methods=['GET', 'POST'])
async def catalogo_categorias():
    async with AsyncSessionLocal() as session:

        if request.method == 'POST':
            form = await request.form
            nombre = form.get('nombreCategoria')
            descripcion = form.get('descripcion')

            if not nombre:
                return jsonify({"error": "El nombre de la categoría es obligatorio"}), 400

            result = await session.execute(
                select(Categoria).where(Categoria.nombre == nombre)
            )
            existe = result.scalar_one_or_none()

            if existe:
                return jsonify({"error": "La categoría ya existe"}), 400

            nueva = Categoria(nombre=nombre, descripcion=descripcion)
            session.add(nueva)
            await session.commit()

            return redirect(url_for('catalogo_categorias.catalogo_categorias'))

        # GET → cargar categorías con productos (eager load)
        result = await session.execute(
            select(Categoria).options(selectinload(Categoria.productos))
        )
        categorias = result.scalars().unique().all()

    return await render_template(
        'catalogo-categorias.html',
        categorias=categorias
    )
