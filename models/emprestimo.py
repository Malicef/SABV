from models.db.db import *
from peewee import *
from models.livro import Livro
from models.usuario import Usuario
class Emprestimo(BaseModel):
    livro = ForeignKeyField(Livro, backref='emprestimos')
    usuario = ForeignKeyField(Usuario, backref='emprestimo')
    data_emprestimo = DateField()
    data_devolucao = DateField(null=True)
    status = CharField()