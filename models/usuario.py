from peewee import *
from models.db.db import *

class Usuario(BaseModel):
    nome = CharField()
    email = CharField()
    senha = CharField()