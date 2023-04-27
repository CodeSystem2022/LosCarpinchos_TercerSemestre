#lectura de archivos, video 4
"""
archivo = open('prueba.txt', 'r', encoding='utf-8')
print(archivo.read())

#lectura de archivos, video 5

archivo = open('prueba.txt', 'x', encoding='utf-8') # x es parar crear el archivo especificado
print(archivo.read())

#letra r= read, a= append, w= write, x= crear, t= para texto o text, b= binary, w+ = scribir y leer, r+ = eleer y escribir

#video 6:
archivo = open('prueba.txt', 'r', encoding='utf-8') # x es parar crear el archivo especificado
# print(archivo.read(5)) #se puede leer determinada cant de digitos
print(archivo.readline()) #va a leer la primer linea de nuestro archivo/si hacemos otro print readline va a leer la 2da linea y sucesivamente

#video 7:
archivo = open('c:\\prueba.txt', 'r', encoding='utf-8') #se puede argregar la ruta al archivo
"""
#video 8:
#vamos a iterar el archivo, cada una de las lineas

archivo = open('prueba.txt', 'r', encoding='utf-8')
# for linea in archivo:
    #print(linea) #aparecen las lineas con espacio
    #print(archivo.readlines()) #tambien podemos devolver una lista / se puede ejecutar fuera del for tambien

print(archivo.readlines()[1]) #podemos hacer print por linea

#video 9:
#anexamos info, copiamos a otro
archivo2 = open('copia.txt', 'a', encoding='utf-8')
archivo2.write(archivo.read())
archivo.close() #cerramos el primer archivo
archivo2.close() #cerramos el segundo archivo

print('Se ha terminado el proceso de leer y copiar archivos') #en leccion02 aparece copia.txt con toda la info copiada
#las veces que copiemos se repite la info a continuación, se anexa a lo que ya exista. Para que no suceda eso podemos
#cambiar la 'a' por la 'w'


