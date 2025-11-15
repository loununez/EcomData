# modules/usuarios/routes.py
from quart import Blueprint, render_template, jsonify
from database.database import AsyncSessionLocal
from models.usuario import Usuario
from models.rol import Rol
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload

usuarios_bp = Blueprint('usuarios', __name__)

@usuarios_bp.route('/')
async def usuarios():
    async with AsyncSessionLocal() as session:
        # Obtener todos los usuarios con sus roles
        result = await session.execute(
            select(Usuario)
            .options(selectinload(Usuario.rol))
        )
        usuarios_list = result.scalars().all()

    return await render_template('usuario.html', usuarios=usuarios_list)