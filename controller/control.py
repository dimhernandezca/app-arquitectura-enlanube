from flask import render_template, request 
from database.db import *

def func_home():
    connectionSQL()
    return render_template("home.html")

def func_register_page():
    return render_template("register.html")
    
def func_consult_page():
    return render_template("consult.html")
    
def func_register_user():
    nombreMascota = request.form["nombreMascota"]
    propietario = request.form["propietario"]
    petType = request.form["petType"]
    raza = request.form["raza"]
    edad = request.form["edad"]
    sexo = request.form["sexo"] 
    resultado = add_user(nombreMascota, propietario, petType, raza, edad, sexo)
    return "OK"