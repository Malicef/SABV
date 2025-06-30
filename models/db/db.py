from peewee import *


sqlite_db = SqliteDatabase('sistema.db', pragmas={'journal_mode': 'wal'})

class BaseModel(Model):
    class Meta:
        database = sqlite_db

database = sqlite_db
