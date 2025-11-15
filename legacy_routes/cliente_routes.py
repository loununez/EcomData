from quart import Blueprint, render_template, request, redirect, url_for, jsonify
from sqlalchemy.future import select
from database.database import AsyncSessionLocal
from models.cliente import Cliente

cliente_bp = Blueprint('cliente_bp', __name__, template_folder='../templates')


# Listado de clientes
@cliente_bp.route('/', methods=['GET'])
async def listado_clientes():
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(Cliente))
        clientes = result.scalars().all()
    return await render_template('listado-clientes.html', clientes=clientes)


# Crear cliente (formulario)
@cliente_bp.route('/nuevo', methods=['GET', 'POST'])
async def nuevo_cliente():
    async with AsyncSessionLocal() as session:
        if request.method == 'GET':
            return await render_template('modal-nuevo-cliente.html')

        # POST: procesar formulario
        form = await request.form
        nombre = form.get('nombre')
        email = form.get('email')
        telefono = form.get('telefono')
        direccion = form.get('direccion')

        # Validar email único
        result = await session.execute(select(Cliente).where(Cliente.email == email))
        cliente_existente = result.scalar_one_or_none()
        if cliente_existente:
            return jsonify({"error": "Ya existe un cliente con ese email"}), 400

        nuevo = Cliente(
            nombre=nombre,
            email=email,
            telefono=telefono,
            direccion=direccion
        )
        session.add(nuevo)
        await session.commit()

    return redirect(url_for('cliente_bp.listado_clientes'))


# Eliminar cliente
@cliente_bp.route('/<int:cliente_id>/eliminar', methods=['POST'])
async def eliminar_cliente(cliente_id: int):
    async with AsyncSessionLocal() as session:
        cliente = await session.get(Cliente, cliente_id)
        if not cliente:
            return jsonify({"error": "Cliente no encontrado"}), 404
        await session.delete(cliente)
        await session.commit()

    return redirect(url_for('cliente_bp.listado_clientes'))
