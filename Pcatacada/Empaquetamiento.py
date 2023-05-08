import cv2
import numpy as np
import socket
import struct

# Configurar la dirección IP del servidor de streaming (quien recibe los frames)
server_address = ('IP O URL A ENVIAR FRAMES', <PUERTO POR DONDE SE ENVIAN>)

# Crear un socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Iniciar la captura de video desde la cámara
cap = cv2.VideoCapture(0)

# Verificar si la cámara está abierta
if not cap.isOpened():
    print("Error al abrir la cámara")
    exit()

# Configurar el códec de video y el ancho y alto del frame
fourcc = cv2.VideoWriter_fourcc(*'XVID')
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# Iniciar la transmisión de video
while True:
    ret, frame = cap.read()
    if ret:
        # Codificar el frame en formato de imagen JPEG
        _, img_encoded = cv2.imencode('.jpg', frame)

        # Obtener el tamaño de la imagen codificada
        data = np.array(img_encoded)
        string_data = data.tobytes()
        size = len(string_data)

        # Enviar la imagen al servidor de streaming en un solo paquete
        sock.sendto(struct.pack('<L', size), server_address)
        sock.sendto(string_data, server_address)

        # Mostrar el frame en una ventana
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Liberar los objetos de captura y escritura de video
cap.release()
cv2.destroyAllWindows()
sock.close()
