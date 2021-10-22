class dev():
    DEBUG = True
    SECRET_KEY = "pyhonflasgrupo5"
    DATABASE = {
        "name": 'db.sqlite3',
        'engine': 'peewee.SqliteDatabase'
    }

class prod():
    DEBUG = True
    SECRET_KEY = "pyhonflasgrupo5"
    DATABASE = {
        "name": 'montemaria.sqlite3',
        'engine': 'peewee.MySqliteDatabase',
        'host': 'url.donde.esta.mi.bd.com',
        'user': 'grupo5mintic',
        'passwd': 'estoesunejemplo'
    }