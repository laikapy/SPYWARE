from flask import Flask, request
import cv2
import requests
import socket
import multiprocessing as mp

app = Flask(_name_)

# Configurar la dirección IP de PC2
dest_ip = 'dirección O URL a conectar'

# Crear un socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Función para la tarea en segundo plano
def start_streaming():
    # Ejecutar pruebaframe.py
    exec(open("pruebaframe.py").read())

# Crear la tarea en segundo plano
streaming_process = mp.Process(target=start_streaming)

@app.route('/Start', methods=['POST'])
def start():
    signal = request.form.get('signal')
    if signal == 'Start' or signal == 'start':
        print('Señal start recibida')
        # Iniciar la tarea en segundo plano para enviar los frames de la cámara a PC2
        streaming_process.start()
        return 'Señal Start recibida correctamente'

    elif signal == 'Stop' or signal == 'stop':
        print('Señal de stop recibida')
        return 'Señal Start recibida correctamente'


    else:
        print('Señal no valida')
        return 'Señal no valida', 400


if _name_ == '_main_':
    # Iniciar el servidor Flask para recibir la señal de inicio
    app.run(host='0.0.0.0', port=8080)
