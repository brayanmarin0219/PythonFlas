from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def Inicio():
    
    #Añadir mision, vision, Valores empresariales 
    return  "Pagina de Inicio "

@app.route('/contacto', methods = ["GET"])
def contato():
    #PQR, DIRECTORIO
    return  "Pagina de Contacto"

@app.route('/contacto/preguntas_frecuentes', methods = ["GET"])
def Preguntas_frecuentes():
    return  "Preguntas frecuentes"

@app.route('/registro', methods = ["GET","POST"])
def Registro():
    return  render_template("/registro.html") 
#REGISTRO YA VA HA TENER EL FORMULARIO

@app.route('/login', methods = ["GET","POST"])
def Login():
<<<<<<< HEAD
    return render_template("login.html")  # html listo
=======
    return  render_template("/login.html") 
>>>>>>> 09e346febb9f55e66cce314a67009064b5f2012c

@app.route('/perfil_paciente', methods = ["GET"])
def Paciente():
    return  "Pagina de Pacientes"

@app.route('/perfil_paciente/citas', methods = ["GET","POST"])
def Citas():
    return  "Pagina de Citas "
#Crear hmtl para crear, y consultar, ver citas 

@app.route('/perfil_paciente/comentarios', methods = ["GET","POST"])
def Comentarios():
    return  "Preguntas Comentarios"
# Crear comentarios y ver comentarios 

@app.route('/perfil_paciente/Datos_personales', methods = ["GET"])
def Datos_personales():
    return  " Datos personales   "
# Crear opcion para actualizar 

@app.route('/perfil_medico', methods = ["GET"])
def Medico():
    return  "Pagina de Medico "

@app.route('/perfil_medico/historia_medica', methods = ["GET","POST"])
def Historia_medica():
    return  "Pagina de Historia Medica "
#Consultar, actualizar y el resto

@app.route('/perfil_medico/citas', methods = ["GET","POST"])
def Citas_1():
    return  "Pagina de Citas "
# Modificar y eliminar 

@app.route('/perfil_medico/Datos_personales', methods = ["GET"])
def Datos_personales_1():
    return  " Datos personales  "
#actualizar 

@app.route('/perfil_superadministrativo', methods = ["GET"])
def superadministrativo () :
    return render_template("/superadmin.html")

@app.route('/perfil_superadministrativo/historia_medica', methods = ["GET","POST"])
def Historia_medica_1():
    return  "Pagina de Historia Medica "
#Crear, consultar, actualizar 

@app.route('/perfil_superadministrativo/usuarios', methods = ["GET","POST"])
def Usuarios_9():
    return "Creacion de usuarios"
    #Crear usuario

@app.route('/perfil_superadministrativo/usuarios/consultar', methods = ["GET","POST"])
def Consultar_9():
    return "Consultar usuarios"

@app.route('/perfil_superadministrativo/usuarios/consultar/editar', methods = ["GET","POST"])
def editar_2():
    return "Editar Usuario"
#eliminar, editar

@app.route('/perfil_superadministrativo/citas', methods = ["GET","POST"])
def Citas_4():
    return  "Pagina de Citas "
#crear, eliminar, editar 


if __name__ == "__main__":
    app.run(debug=True)