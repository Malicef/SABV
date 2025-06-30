from flask import Blueprint, render_template, request, redirect, session, url_for
from models.admin import ADM

admin_bp = Blueprint("admin", __name__)

@admin_bp.route("/admin/login", methods=["GET", "POST"])
def login_admin():
    if request.method == "POST":
        email = request.form["email"]
        senha = request.form["senha"]
        admin = ADM.get_or_none(ADM.email == email, ADM.senha == senha)
        if admin:
            print("opa")
            session["admin_id"] = admin.id
            return redirect(url_for("livros.index_admin"))
        return "Login inválido", 401
    return render_template("login_admin.html")

@admin_bp.route("/admin/logout")
def logout_admin():
    session.pop("admin_id", None)
    return redirect(url_for("admin.login_admin"))
