from app import *

@app.cli.command("crear_datos_iniciales")
def crear_datos_iniciales():
    db.init_app(app)
    u1 = Usuario.get_or_create(
        username = "u1",
        nombre = "u1",
        email = "u1@usermintic.com",
        password = "u1u1u1",
        rol = 2 # 0:admin, 1:docor, 2:usuario
    )
    print(u1)

app.cli()