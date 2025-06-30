from models.db.db import BaseModel 
from peewee import CharField

class ADM(BaseModel):
    senha = CharField()
    email = CharField()