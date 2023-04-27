# Declaramos una variable

"""
try:
    archivo = open('prueba.txt', 'w') #w es write
except BaseException as e:
    print(e)
finally: #siempre se ejecuta
    archivo.close() #con esto se debe cerrar el archivo
#cuando le damos run se crea el archivo txt
"""
"""
#AGREGAR INFO AL ARCHIVO TXT

try:
    archivo = open('prueba.txt', 'w') #w es write
    archivo.write('Programamos con diferentes tipos de archivos, ahora en txt.\n')
    archivo.write('Con esto terminamos.')
except BaseException as e:
    print(e)
finally: #siempre se ejecuta
    archivo.close() #con esto se debe cerrar el archivo

"""

#video 3
#los acentos no aparecen a menos que arreglemos el UTF-8
try:
    archivo = open('prueba.txt', 'w', encoding='utf-8') #w es write
    archivo.write('Programamos con diferentes tipos de archivos, ahora en txt.\n')
    archivo.write('Los acentos son importantes para las palabras\n')
    archivo.write('como por ejemplo: acción, ejecución y producción\n')
    archivo.write('Con esto terminamos.')
    archivo.write('Saludos a todos los alumnos de la tecnicatura.')
except BaseException as e:
    print(e)
finally: #siempre se ejecuta
    archivo.close() #con esto se debe cerrar el archivo
# archivo.write('Todo quedo perfecto.') # si ejecutamos con esta linea da error, no se puede seguir agregando en un programa cerrado.


