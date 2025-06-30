from models.db.db import *
from peewee import IntegerField, CharField

class Livro(BaseModel):
    titulo = CharField()
    autor = CharField()
    resumo = CharField()
