import os
import serial
import time

# Lectura archivos
def leer_archivos_carpeta(ruta_carpeta):
    contenido = []
    archivos = os.listdir(ruta_carpeta)
    print(archivos)
    for archivo in archivos:
        ruta_archivo = os.path.join(ruta_carpeta, archivo)
        if os.path.isfile(ruta_archivo):
            with open(ruta_archivo, 'r') as f:
                contenido.append(f.readlines())
    return contenido

carpeta = 'Archivos_de_memoria/'
contenido = leer_archivos_carpeta(carpeta)
print("Hay",len(contenido),"fotogramas en el video.")
print("Hay",len(contenido[9]),"lineas por fotograma.")

# Transmisión
tx = serial.Serial('/dev/ttyUSB1', 115200)
time.sleep(3)
for frame in contenido:
    print("CAMBIO")
    for linea in frame:
        linea_byte = str(int(linea, 2)).encode()
        tx.write(linea_byte)
        tx.write(b'_')
        #time.sleep(0.003) #tiempo de envio max
        #time.sleep(0.1) #tiempo de envio pruebas
        
tx.close()

