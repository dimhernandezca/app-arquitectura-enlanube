from flask import render_template, request 
from database.db import *

def func_home():
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
    sexo = request.form["sexo"] 
    edad = request.form["edad"]
    print(nombreMascota, propietario, petType, raza, sexo, edad)
    confirm_user = add_user(nombreMascota, propietario, petType, raza, sexo, edad)
    if confirm_user:
        return "<h1>The user was created sucessfully</h1>"
    else:
        return "<h1>Error: The user was not created</h1>"

def func_consult_user():
    obj_mascota = request.get_json()
    mascota = obj_mascota["mascota"]
    propietario = obj_mascota["propietario"]
    print(mascota)
    print(propietario)
    consult_user(mascota, propietario)
    return "OK"
    
