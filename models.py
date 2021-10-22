from peewee import *
from playhouse.flask_utils import FlaskDB

db = FlaskDB()

class Usuario(db.Model):
    username = TextField(primary_key=True)
    nombre = TextField()
    email = TextField()
    password = TextField()
    rol = IntegerField() # 0:admin, 1:docor, 2:usuario