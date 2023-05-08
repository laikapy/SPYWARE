import socket
from flask import Flask, Response, render_template
import numpy as np
import cv2
import traceback
app = Flask(__name__)

# Define los detalles de tu socket aquí
HOST = 'IP de la pc en donde se ejecuta'
PORT = 5000

# Define el tamaño máximo de los paquetes que se enviarán por el socket
max_packet_size = 65536

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stream')
def stream():
    def generate():
        print("Pruebas")
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((HOST, PORT))
        while True:
            try:
                data, _ = sock.recvfrom(max_packet_size)
                nparr = np.frombuffer(data, np.uint8)
                img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
                if img is not None:
                    ret, jpeg = cv2.imencode('.jpg', img)
                    yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n')

            except:
                traceback.print_exc()
    return Response(generate(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
