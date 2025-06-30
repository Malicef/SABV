from models.admin import ADM
from models.livro import Livro
from models.emprestimo import Emprestimo
from models.usuario import Usuario
from models.db.db import database

from controllers.admin_controller import admin_bp
from controllers.livro_controller import livro_bp
from controllers.emprestimo_controller import emprestimo_bp
from controllers.usuario_controller import usuario_bp

def inicializar_db(database):
    database.connect()
    database.create_tables([ADM, Livro, Emprestimo, Usuario])

    if not ADM.get_or_none(ADM.email == "admin@teste.com"):
        ADM.create(email="admin@teste.com", senha="1234")

    if not Usuario.get_or_none(Usuario.email == "usuario@teste.com"):
        Usuario.create(nome="Usuário Teste", email="usuario@teste.com", senha="1234")


def configura_rotas(app):
    app.register_blueprint(admin_bp)
    app.register_blueprint(livro_bp, url_prefix="/livros")
    app.register_blueprint(emprestimo_bp)
    app.register_blueprint(usuario_bp)

def configure_all(app):
    inicializar_db(database=database)
    configura_rotas(app)