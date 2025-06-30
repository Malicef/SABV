from flask import Blueprint, render_template, request, redirect, url_for, session
from models.emprestimo import Emprestimo
from models.livro import Livro
from datetime import date

emprestimo_bp = Blueprint("emprestimos", __name__)

@emprestimo_bp.route("/usuario/emprestar/<int:livro_id>", methods=["POST"])
def solicitar_emprestimo(livro_id):
    if "usuario_id" not in session:
        return redirect(url_for("usuario.login_usuario"))
    Emprestimo.create(
        livro=livro_id,
        usuario=session["usuario_id"],
        data_emprestimo=date.today()
    )
    return redirect(url_for("livros.index_usuario"))

@emprestimo_bp.route("/admin/emprestimos")
def ver_emprestimos():
    if "admin_id" not in session:
        return redirect(url_for("admin.login_admin"))
    emprestimos = Emprestimo.select()
    return render_template("emprestimos/solicitacoes.html", emprestimos=emprestimos)

@emprestimo_bp.route("/admin/emprestimos/aprovar/<int:id>", methods=["POST"])
def aprovar(id):
    emprestimo = Emprestimo.get_or_none(Emprestimo.id == id)
    if emprestimo:
        emprestimo.status = "aceito"
        emprestimo.save()
    return redirect(url_for("emprestimos.ver_emprestimos"))
