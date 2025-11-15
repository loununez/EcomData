from quart import Blueprint, render_template, request, redirect, url_for, jsonify
from sqlalchemy.future import select
from database.database import AsyncSessionLocal
from models.usuario import Usuario
from models.rol import Rol
import bcrypt

usuarios_agregar_bp = Blueprint('usuarios_agregar', __name__)

# Renderiza el formulario
@usuarios_agregar_bp.route('/')
async def usuarios_agregar():
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(Rol))
        roles = result.scalars().all()
    return await render_template('usuario-agregar-usuario.html', roles=roles)

# Procesa el formulario (POST)
@usuarios_agregar_bp.route('/guardar', methods=['POST'])
async def guardar_usuario():
    form = await request.form
    nombre = form.get('nombre')
    email = form.get('email')
    password = form.get('password')
    rol_nombre = form.get('rol')

    async with AsyncSessionLocal() as session:
        result = await session.execute(select(Rol).where(Rol.nombre == rol_nombre))
        rol = result.scalar_one_or_none()

        if not rol:
            return jsonify({"error": "Rol no encontrado"}), 400

        hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        nuevo_usuario = Usuario(
            nombre=nombre,
            email=email,
            password=hashed_pw,
            rol_id=rol.id
        )

        session.add(nuevo_usuario)
        await session.commit()

    return redirect(url_for('usuarios.usuarios'))