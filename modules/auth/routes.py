from quart import Blueprint, render_template, request, redirect, url_for, session, jsonify
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from database.database import AsyncSessionLocal
from models import Usuario
import bcrypt

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/", methods=["GET"])
async def login_page():
    return await render_template("index.html")

@auth_bp.route("/login", methods=["GET"])
async def login_get():
    return await render_template("login.html")

@auth_bp.route("/login", methods=["POST"])
async def login():
    """Handle login with both form and JSON requests"""
    try:
        # Try to get JSON data first
        if request.content_type and 'application/json' in request.content_type:
            data = await request.get_json()
            email = data.get("email") or data.get("usuario")
            password = data.get("password") or data.get("contrasena")
        else:
            form = await request.form
            email = form.get("usuario")
            password = form.get("contrasena")

        if not email or not password:
            return jsonify({"success": False, "message": "Email and password are required"}), 400

        async with AsyncSessionLocal() as session_db:
            result = await session_db.execute(
                select(Usuario).options(selectinload(Usuario.rol)).where(Usuario.email == email)
            )
            usuario = result.scalars().first()

            if usuario:
                # Check password - handle both bcrypt and plain text for compatibility
                password_match = False
                try:
                    password_match = bcrypt.checkpw(password.encode('utf-8'), usuario.password.encode('utf-8'))
                except:
                    password_match = usuario.password == password
                
                if password_match:
                    session["usuario_id"] = usuario.id
                    session["user_email"] = usuario.email
                    session["rol"] = usuario.rol.nombre if usuario.rol else "usuario"
                    
                    # Return JSON response for AJAX requests
                    if request.content_type and 'application/json' in request.content_type:
                        return jsonify({"success": True, "message": "Login successful", "redirect": "/panel"}), 200
                    else:
                        return redirect(url_for("panel.panel"))
            
            # Invalid credentials
            if request.content_type and 'application/json' in request.content_type:
                return jsonify({"success": False, "message": "Invalid email or password"}), 401
            else:
                return await render_template("index.html", error="Credenciales inválidas")
    except Exception as e:
        if request.content_type and 'application/json' in request.content_type:
            return jsonify({"success": False, "message": f"Error: {str(e)}"}), 500
        else:
            return await render_template("index.html", error="Error during login")


@auth_bp.route("/logout", methods=["GET", "POST"])
async def logout():
    session.clear()
    if request.content_type and 'application/json' in request.content_type:
        return jsonify({"success": True, "message": "Logout successful", "redirect": "/auth/login"}), 200
    else:
        return redirect(url_for("auth.login_page"))

@auth_bp.route("/check-session", methods=["GET"])
async def check_session():
    """Check if user is logged in"""
    if "usuario_id" in session:
        return jsonify({
            "logged_in": True, 
            "user_email": session.get("user_email"),
            "user_id": session.get("usuario_id"),
            "rol": session.get("rol")
        }), 200
    else:
        return jsonify({"logged_in": False}), 200
