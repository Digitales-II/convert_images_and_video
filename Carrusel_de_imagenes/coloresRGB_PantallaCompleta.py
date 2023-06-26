import math

def procesar_archivo(archivo_entrada, archivo_salida):
    with open(archivo_entrada, 'r') as entrada, open(archivo_salida, 'w') as salida:
        lineas_entrada = entrada.readlines()
        total_lineas = len(lineas_entrada)
    
        for num_linea in range(3200):
            num1 = obtener_numeros(lineas_entrada[num_linea])
            num2 = obtener_numeros(lineas_entrada[num_linea+3200])
            num3 = obtener_numeros(lineas_entrada[num_linea+6400])
            num4 = obtener_numeros(lineas_entrada[num_linea+9600])
            for i in range(3):
                bin1 = binarizar(num1[i])
                bin1 = bin1.zfill(3)
                salida.write(bin1)
            for i in range(3):
                bin2 = binarizar(num2[i])
                bin2 = bin2.zfill(3)
                salida.write(bin2) 
            for i in range(3):
                bin3 = binarizar(num3[i])
                bin3 = bin3.zfill(3)
                salida.write(bin3) 
            for i in range(3):
                bin4 = binarizar(num4[i])
                bin4 = bin4.zfill(3)
                salida.write(bin4)  
            salida.write('\n')
    


def obtener_numeros(linea):
    inicio = linea.index('(') + 1
    fin = linea.index(')')
    numeros_str = linea[inicio:fin].split(',')
    numeros = [int(int(numero)/34) for numero in numeros_str]
    return numeros

def binarizar(decimal):
    binario = ''
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario

archivo_entrada1 = 'Fotogramas_txt/prueba.txt'
archivo_salida1 = 'Archivos_de_memoria/a.txt'

archivo_entrada2 = 'Fotogramas_txt/prueba2.txt'
archivo_salida2 = 'Archivos_de_memoria/b.txt'

archivo_entrada3 = 'Fotogramas_txt/prueba3.txt'
archivo_salida3 = 'Archivos_de_memoria/c.txt'

archivo_entrada4 = 'Fotogramas_txt/prueba4.txt'
archivo_salida4 = 'Archivos_de_memoria/d.txt'

archivo_entrada5 = 'Fotogramas_txt/prueba5.txt'
archivo_salida5 = 'Archivos_de_memoria/e.txt'

archivo_entrada6 = 'Fotogramas_txt/prueba6.txt'
archivo_salida6 = 'Archivos_de_memoria/f.txt'

archivo_entrada7 = 'Fotogramas_txt/prueba7.txt'
archivo_salida7 = 'Archivos_de_memoria/g.txt'

archivo_entrada8 = 'Fotogramas_txt/prueba8.txt'
archivo_salida8 = 'Archivos_de_memoria/h.txt'

archivo_entrada9 = 'Fotogramas_txt/prueba9.txt'
archivo_salida9 = 'Archivos_de_memoria/i.txt'

archivo_entrada10 = 'Fotogramas_txt/prueba10.txt'
archivo_salida10 = 'Archivos_de_memoria/j.txt'



procesar_archivo(archivo_entrada1, archivo_salida1)
procesar_archivo(archivo_entrada2, archivo_salida2)
procesar_archivo(archivo_entrada3, archivo_salida3)
procesar_archivo(archivo_entrada4, archivo_salida4)
procesar_archivo(archivo_entrada5, archivo_salida5)
procesar_archivo(archivo_entrada6, archivo_salida6)
procesar_archivo(archivo_entrada7, archivo_salida7)
procesar_archivo(archivo_entrada8, archivo_salida8)
procesar_archivo(archivo_entrada9, archivo_salida9)
procesar_archivo(archivo_entrada10, archivo_salida10)



