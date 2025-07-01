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

    
        
def criar_tabelas_teste():
    if not ADM.get_or_none(ADM.email == "admin@teste.com"):
        ADM.create(email="admin@teste.com", senha="1234")
    if not Usuario.get_or_none(Usuario.email == "usuario@teste.com"):
        Usuario.create(nome="Usuário Teste", email="usuario@teste.com", senha="1234")
    if not Livro.get_or_none(Livro.titulo == "Livro de Teste"):
        Livro.create(titulo="Livro de Teste", autor="Autor Teste", resumo="Resumo do Livro de Teste")
    if not Emprestimo.get_or_none(Emprestimo.livro == Livro.get(Livro.titulo == "Livro de Teste")):
        Emprestimo.create(livro=Livro.get(Livro.titulo == "Livro de Teste"),
                          usuario=Usuario.get(Usuario.email == "usuario@teste.com"),
                            data_emprestimo="2023-10-01",
                            data_devolucao=None,
                            status="pendente")
    


def configura_rotas(app):
    app.register_blueprint(admin_bp)
    app.register_blueprint(livro_bp, url_prefix="/livros")
    app.register_blueprint(emprestimo_bp)
    app.register_blueprint(usuario_bp)

def configure_all(app):
    inicializar_db(database=database)
    criar_tabelas_teste()
    configura_rotas(app)