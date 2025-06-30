from flask import Blueprint, render_template, redirect, request, session, url_for
from models.usuario import Usuario

usuario_bp = Blueprint("usuario", __name__)

@usuario_bp.route("/usuario/login", methods=["GET", "POST"])
def login_usuario():
    if request.method == "POST":
        email = request.form["email"]
        senha = request.form["senha"]
        user = Usuario.get_or_none(Usuario.email == email, Usuario.senha == senha)
        if user: 
            session["usuario_id"] = user.id
            return redirect(url_for("livros.index_usuario"))
        return "Login invalido", 401
    return render_template("login_usuario.html")

@usuario_bp.route("/usuario/logout")
def logout_usuario():
    session.pop("usuario_id", None)
    return redirect(url_for("usuario.login_usuario"))