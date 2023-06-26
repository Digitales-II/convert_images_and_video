import os
import serial
import time

# Lectura archivos
def leer_archivos_carpeta(ruta_carpeta):
    contenido = []
    archivos = os.listdir(ruta_carpeta)
    archivos.sort()
    print(archivos)
    for archivo in archivos:
        ruta_archivo = os.path.join(ruta_carpeta, archivo)
        if os.path.isfile(ruta_archivo):
            with open(ruta_archivo, 'r') as f:
                contenido.append(f.readlines())
    return contenido

carpeta = 'numeros/'
contenido = leer_archivos_carpeta(carpeta)
print("Hay",len(contenido),"fotogramas en el video.")
print("Hay",len(contenido[9]),"lineas por fotograma.")

# Transmisión
tx = serial.Serial(port     = '/dev/ttyUSB0', 
                   baudrate = 115200,
                   timeout  = 5)
time.sleep(3)

# Enviar frames del video
for frame in contenido:
    inicio = time.time()
    for linea in frame:
        linea_byte = str(int(linea, 2)).encode()
        tx.write(linea_byte)
        tx.write(b'_')
    fin = time.time()
    demora = fin - inicio
    print("CAMBIO A FRAME",contenido.index(frame),"en",str(round((demora),4)),"segundos.")
    time.sleep(3.35 - demora)

#Blanquear memoria
for i in range(3200*10):
    tx.write('0'.encode())
    tx.write(b'_')

      
tx.close()
