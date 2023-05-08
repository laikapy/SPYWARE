import pyfiglet
from termcolor import colored
from PIL import Image
import gzip
import base64
import math

def title():
    met = pyfiglet.figlet_format("SilentEye", font="banner3-d", width=100)
    print(colored(met, 'red'))
def imgtxt():
    # Abrir la imagen y convertirla a escala de grises
    imagen = Image.open('calabera.PNG').convert('L')

    # Definir los caracteres a usar para representar los niveles de brillo
    caracteres = [' ', '.', ':', '-', '=', '+', '*', '#', '%', '@']

    # Obtener el ancho y la altura de la imagen
    ancho, altura = imagen.size

    # Crear un archivo de texto para escribir la representación de la imagen
    with open('nombre_del_archivo.txt', 'w') as archivo:
        # Recorrer la imagen píxel por píxel y escribir los caracteres correspondientes
        for y in range(altura):
            for x in range(ancho):
                # Obtener el valor de intensidad de gris del píxel
                intensidad = imagen.getpixel((x, y))
                # Obtener el índice del caracter que representa el valor de intensidad
                indice_caracter = int(intensidad / 25)
                # Escribir el caracter en el archivo
                archivo.write(caracteres[indice_caracter])
            archivo.write('\n')
def eye():
    # abrir el archivo y leer su contenido
    with open('img.txt', 'r') as f:
        contenido = f.read()

    # imprimir el contenido en color rojo
    print(colored(contenido, 'red'))




