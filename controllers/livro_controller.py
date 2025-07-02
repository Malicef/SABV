from flask import Blueprint, render_template, request, redirect, url_for, session
from models.livro import Livro

livro_bp = Blueprint("livros", __name__)

# Lista para Admin com opções de edição e exclusão
@livro_bp.route("/admin/livros")
def index_admin():
    if "admin_id" not in session:
        return redirect(url_for("admin.login_admin"))
    livros = Livro.select()
    return render_template("livros/index_admin.html", livros=livros)

# Lista para Usuário comum
@livro_bp.route("/usuario/livros")
def index_usuario():
    if "usuario_id" not in session:
        return redirect(url_for("usuario.login_usuario"))
    livros = Livro.select()
    return render_template("livros/index_usuario.html", livros=livros)

@livro_bp.route("/admin/livros/criar", methods=["GET", "POST"])
def criar():
    if "admin_id" not in session:
        return redirect(url_for("admin.login_admin"))
    if request.method == "POST":
        Livro.create(
            titulo=request.form["titulo"],
            autor=request.form["autor"],
            resumo=request.form["resumo"]
        )
        return redirect(url_for("livros.index_admin"))
    return render_template("livros/criar.html")

@livro_bp.route("/admin/livros/deletar/<int:id>", methods=["POST"])
def deletar(id):
    if "admin_id" not in session:
        return redirect(url_for("admin.login_admin"))
    livro = Livro.get_or_none(Livro.id == id)
    if livro:
        # livro.delete_instance()
        return redirect(url_for("livros.index_admin"))

@livro_bp.route("/admin/livros/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    if "admin_id" not in session:
        return redirect(url_for("admin.login_admin"))
    
    livro = Livro.get_or_none(Livro.id == id)
    if not livro:
        return "Livro não encontrado", 404

    if request.method == "POST":
        livro.titulo = request.form["titulo"]
        livro.autor = request.form["autor"]
        livro.resumo = request.form["resumo"]
        livro.save()
        return redirect(url_for("livros.index_admin"))

    return render_template("livros/editar.html", livro=livro)

@livro_bp.route("/livros/<int:id>")
def visualizar(id):
    livro = Livro.get_or_none(Livro.id == id)
    if not livro:
        return "Livro não encontrado", 404
    return render_template("livros/visualizar.html", livro=livro)

@livro_bp.route("/livros")
def listar_livros():
    livros = Livro.select() 
    return render_template("livros/listar.html", livros=livros)

