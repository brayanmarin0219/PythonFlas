from flask import Flask
from flask import render_template
from flask import redirect
from flask import request

from models import *
from config import dev
import flask_login

app = Flask(__name__)
app.config.from_object(dev)

db.init_app(app)

usuarios = {
    1: {
        "nombre": "brayan",
        "tipoUsuario": "medico",
        "usuario": "email",
        "password": "contrasena"
    }
}

citas = {
    1: {
        "fecha": "date",
        "medico": "nombre medico",
        "paciente": "nombre paciente"
    }
}

comentarios = {
    1: {
        "idCita": "referencia de cita",
        "mensaje": "mensaje del comentario"
    }
}

@app.route('/')
def Inicio():
    
    #Añadir mision, vision, Valores empresariales 
    return  render_template("/inicio.html")

@app.route('/contacto', methods = ["GET"])
def contato():
    #PQR, DIRECTORIO
    return  render_template("/contacto.html")

@app.route('/contacto/preguntas_frecuentes', methods = ["GET"])
def Preguntas_frecuentes():
    return  render_template("/FAQ.html")

@app.route('/registro', methods = ["GET","POST"])
def Registro():
    return  render_template("/registro.html") 
#REGISTRO YA VA HA TENER EL FORMULARIO

@app.route('/login', methods = ["GET","POST"])
def Login():
    return  render_template("/login.html") 

@app.route('/perfil_paciente', methods = ["GET"])
def Paciente():
    return  render_template("/Perfil_pacientes.html")

@app.route('/perfil_paciente/citas', methods = ["GET","POST"])
def Citas():
    return  render_template("/Citas.html")
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
    return  render_template("/Medico.html")

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
    return render_template("/superadmin_usuarios.html")
    #Crear usuario

@app.route('/perfil_superadministrativo/usuarios/consultar', methods = ["GET","POST"])
def Consultar_9():
    return render_template("/super_admin_consultar.html")

@app.route('/perfil_superadministrativo/usuarios/consultar/editar', methods = ["GET","POST"])
def editar_2():
    return render_template("/superadmin_editar_usuario.html")
#eliminar, editar

@app.route('/perfil_superadministrativo/citas', methods = ["GET","POST"])
def Citas_4():
    return  "Pagina de Citas "
#crear, eliminar, editar 


if __name__ == "__main__":
    app.run()