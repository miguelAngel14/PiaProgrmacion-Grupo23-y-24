import re
#se encarga de exportar de las expresiones regulares
import csv
#esta funcion se encarga de exportar archivos de texto 
import os
#esta funcion es la encargada de llamar al sistema operativo 
import datetime
#se encarga de exportar los datos de datetime
import json
#exporta librerias por medio de listas,diccionarios etc
from operator import attrgetter
from typing import List
from clasepia import CONTACTO
conj_contactos=[]

def cargar_archivo():
    with open('contactos_mobil.csv') as archivo_csv:
        lector_csv = csv.reader(archivo_csv, delimiter = "|")
        contador_lineas = 0
        # se creo una lista vacia.
        # lectura sencuncial.
        for linea_datos in lector_csv:
            if contador_lineas == 0:
                # Si es la primer línea, muestro los nombres de campo y no guardo nada
                # se establecio la lista 
                print(f'Los nombres de columna son {", ".join(linea_datos)}')
            else:
                objeto_temporal = CONTACTO(linea_datos[0],linea_datos[1],linea_datos[2],linea_datos[3], linea_datos[4],linea_datos[5])
                conj_contactos.append(objeto_temporal)
        # Se incrementa el número de líneas, pase lo que pase.
            contador_lineas += 1
    print(f'Procesadas {len(conj_contactos)}líneas.')
    input("PRESIONA ENTER PARA CONTINUAR...")

# se creo el menu con 5 opciones para el usuario y la OS es el encargo de limpiar la pantalla
def Menu_Principal():
    while True:
        os.system ("cls")
        print("MENU CONTACTOS")
        print("[1] Agregar un contacto")
        print("[2] Buscar un contacto")
        print("[3] Eliminar un contacto")
        print("[4] Mostrar contactos")
        print("[5] Serializar datos")
        print("[0] Salir")
        _resp= int(input("Opcion: "))

        if _resp == 1:
            Agregar_Contacto()
        elif _resp== 2:
            Buscar_Contacto()
        elif _resp== 3:
            Eliminar_Contacto()
        elif _resp== 4:
            Mostrar_Contactos()
        elif _resp == 5:
            Serializar_Contacto()
        elif _resp == 0:
            print("Se ordenaron los contactos por NickName")
            ordenar()
            cambiar_archivo()
            escribir_archivo()
            print("Se guardaron los contactos en: contactos_mobil.csv ")
            break
        else:
            print("Opcion Invalida\nIntente de nuevo")

def Validar(_pregunta,_type):
    _captura=""
    #procesamiento para los datos de Nickname
    if _type=="nickname":
        _check="^[A-Z|a-z]{1}[a-z|A-Z|0-9]{4,15}$" #^ para empezar la expression
        while True:                             #[] se almacenan conjunto de caracteres
            _captura=input(_pregunta)           #{} se almacena la cantidad de caracteres
            if re.search(_check,_captura):      #$ el final
                return (_captura)
                break
            else:
                print("El dato no tiene el tipo correcto")
    #procesamiento para telefono
    if _type=="telefono":
        _check="^[0-9]{2}[ ]{1}[0-9]{4}[-]{1}[0-9]{4}$"
        while True:
            _captura=input(_pregunta)
            if re.search(_check,_captura):
                return _captura
                break
            else:
                print("El dato no tiene el tipo correcto")
    #procesamiento para procesar el nombre 
    if _type=="nombre":
        _check="^[A-Z ]{10,35}$"
        while True:
            _captura=input(_pregunta)
            captura_up= _captura.upper()
            if re.search(_check,captura_up):
                return captura_up
                break
            else:
                print("El dato no tiene el tipo correcto")
    # Procesamiento para float
    if _type=="float":
        _check="^[0-9]\d*\d.\d{1,2}$"
        while True:
            _captura=input(_pregunta)
            if re.search(_check,_captura):
                return float(_captura)
                break
            else:
                print("El dato no tiene el tipo correcto")
    # Procesamiento para la fecha en date
    if _type=="date":
        while True:
            _check="^[0-9]{4}/[0-9]{2}/[0-9]{2}$"
            _captura=input(_pregunta)
            if re.search(_check,_captura):
                    try:
                        anio=int(_captura[0:4])
                        mes=int(_captura[5:7])
                        dia=int(_captura[-2:])
                        return datetime.date(anio,mes,dia)
                    except ValueError:
                        print("El dato no es una fecha calendario correcta")
            else:
                print("El dato no tiene formato correcto AAAA/MM/DD")
    # Procesamiento para email
    if _type=="email":
        _check="^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        while True:
            _captura=input(_pregunta)
            if re.search(_check,_captura):
                return _captura
                break
            else:
                print("El dato no tiene formato de correo")

def Agregar_Contacto():
    os.system ("cls")
    #llamas a la funcion validar(pregunta, el formato)
    nickname= Validar("dame el nickname: ","nickname")
    nombre= Validar("dame el nombre: ","nombre")
    correo= Validar("dame el correo: ","email")
    telefono= Validar("dame el telefono(99 9999-9999): ","telefono")
    fecha_nacimiento= Validar("dame la fecha de naciemiento(AAAA/MM/DD): ","date")
    gasto= Validar("dame los gastos del mes (0.00):","float")
    # se agrega a la lista como objeto
    obj_temp= CONTACTO(nickname,nombre,correo,telefono,fecha_nacimiento,gasto)
    conj_contactos.append(obj_temp)
#busca los contactos en caso de que el contacto no este el ciclo es falso y regresa
def Buscar_Contacto():
    while True:
        os.system ("cls")
        print("BUSQUEDA DE CONTACTOS")
        print("BUSCAR POR:")
        print("(1) NICKNAME")
        print("(2) TELEFONO")
        _resp = input("opcion: ")
        concidencia= False
        if _resp=="1":
            nickname= Validar("dame el nickname: ","nickname")
            for i in conj_contactos:
                if i.NickName==nickname:
                    print(i.NickName,"|",i.Nombre,"|",i.Correo,"|",i.Telefono,"|",i.FechaNacimiento,"|",i.Gasto)
                    concidencia= True
                    break
            break
        elif _resp=="2":
            telefono= Validar("dame el telefono(99 9999-9999): ","telefono")
            for i in conj_contactos:
                if i.Telefono== telefono:
                    print(i.NickName,"|",i.Nombre,"|",i.Correo,"|",i.Telefono,"|",i.FechaNacimiento,"|",i.Gasto)
                    concidencia= True
                    break
            break
        else:
            print("opcion invalida")
    if concidencia== False:
        print("contacto no encontrado")
    input("PRESIONA ENTER PARA CONTINUAR")

def Eliminar_Contacto():
    os.system ("cls")
    print("ELIMINAR CONTACTO")
    telefono= Validar("dame el telefono(99 9999-9999): ","telefono")
    concidencia= False
    for contact in conj_contactos:
        if contact.Telefono== telefono:
            conj_contactos.remove(contact)
            concidencia= True
            break
    if concidencia== True:
        print("contacto eliminado")
    else:
        print("contacto no encontrado")

    input("PRESIONA ENTER PARA CONTINUAR...")

def Mostrar_Contactos():
    os.system("cls")
    for contact in conj_contactos:
        print("NICKNAME: ",contact.NickName)
        print("NOMBRE: ",contact.Nombre)
        print("CORREO: ",contact.Correo)
        print("TELEFONO:",contact.Telefono)
        print("FECHA DE NACIMIENTO: ",contact.FechaNacimiento)
        print("GASTO: ",contact.Gasto)
        print("-"*40)
    input("PRESIONA ENTER PARA CONTINUAR...")

def Serializar_Contacto():
    os.system("cls")
    print("serializar datos a archivo json")
    json_data = json.dumps(conj_contactos, default=lambda o: o.__dict__, indent=4)
    print(json_data)
    input("PRESIONA ENTER PARA CONTINUAR")

def ordenar():
    conj_contactos.sort(key= attrgetter("NickName"), reverse= False)
    Mostrar_Contactos()

def cambiar_archivo():
    ruta_archivo=os.path.abspath(os.getcwd())
    archivo_respaldo=ruta_archivo+"\\contactos_mobil.bak"
    archivo_normal=ruta_archivo+"\\contactos_mobil.csv"

    print(archivo_respaldo)
    print(archivo_normal)

    # Si hay archivo de datos.
    if os.path.exists(archivo_normal):
    # verifica si hay respaldo, y lo elimina
        if os.path.exists(archivo_respaldo):
            os.remove(archivo_respaldo)
        # Pasa el archivo normal, para que sea archivo de respaldo
            os.rename(archivo_normal,archivo_respaldo)

# Genera el archivo CSV.
    f = open(archivo_normal,"w+")
# Escribir el encabezado.
    f.write("NICKNAME|NOMBRE|CORREO|TELEFONO|FECHANACIMIENTO|GASTO")
# Cierra el archivo 
    f.close()

def escribir_archivo():
    ruta = os.path.abspath(os.getcwd())
    archivo_trabajo=ruta+"\\contactos_mobil.csv"
    archivo_respaldo=ruta+"\\contactos_mobil.bak"

# Determinar si el archivo de trabajo ya existe.
    if os.path.exists(archivo_trabajo):
    # Si el archivo existe, entonces verifico si hay respaldo y lo borro.
        if os.path.exists(archivo_respaldo):
            os.remove(archivo_respaldo)

    # Establezco el achivo de datos, como respaldo
        os.rename(archivo_trabajo,archivo_respaldo)

# Genera el archivo CSV
    f = open(archivo_trabajo,"w+")
# Escribo los encabezados de mi CSV
    f.write("NICKNAME|NOMBRE|CORREO|TELEFONO|FECHANACIMIENTO|GASTO\n")
# Escribimos en el CSV, a partir de la lista de objetos.
    for elemento in conj_contactos:
        f.write(f'{elemento.NickName}|{elemento.Nombre}|{elemento.Correo}|{elemento.Telefono}|{elemento.FechaNacimiento}|{elemento.Gasto}\n')

# Cierra el archivo
    f.close()
cargar_archivo()
#menuprincipal
Menu_Principal()
