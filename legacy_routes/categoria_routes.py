from quart import Blueprint, render_template, request, redirect, url_for, jsonify
from sqlalchemy.future import select
from database.database import AsyncSessionLocal
from models.categoria import Categoria

categoria_bp = Blueprint('categoria_bp', __name__, template_folder='../templates')


# Listado de categorías
@categoria_bp.route('/', methods=['GET'])
async def listado_categorias():
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(Categoria))
        categorias = result.scalars().all()
    return await render_template('listado-categorias.html', categorias=categorias)


# Crear categoría (formulario)
@categoria_bp.route('/nuevo', methods=['GET', 'POST'])
async def nueva_categoria():
    async with AsyncSessionLocal() as session:
        if request.method == 'GET':
            return await render_template('modal-nueva-categoria.html')

        # POST: procesar formulario
        form = await request.form
        nombre = form.get('nombre')
        descripcion = form.get('descripcion')

        # Validar nombre único
        result = await session.execute(select(Categoria).where(Categoria.nombre == nombre))
        categoria_existente = result.scalar_one_or_none()
        if categoria_existente:
            return jsonify({"error": "Ya existe una categoría con ese nombre"}), 400

        nueva = Categoria(nombre=nombre, descripcion=descripcion)
        session.add(nueva)
        await session.commit()

    return redirect(url_for('categoria_bp.listado_categorias'))


# Eliminar categoría
@categoria_bp.route('/<int:categoria_id>/eliminar', methods=['POST'])
async def eliminar_categoria(categoria_id: int):
    async with AsyncSessionLocal() as session:
        categoria = await session.get(Categoria, categoria_id)
        if not categoria:
            return jsonify({"error": "Categoría no encontrada"}), 404
        await session.delete(categoria)
        await session.commit()

    return redirect(url_for('categoria_bp.listado_categorias'))
