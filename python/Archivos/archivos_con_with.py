#video 10 clase 2:
##manejo de contexto with, se cierra de forma automatica el archivo
#with open('prueba.txt', 'r', encoding='utf-8') as archivo: #se renombra la variable
    #print(archivo.read())
#es una sintaxis simplificada
#no hace falta ni el try, ni el finally
#en el contexto de with lo que se ejecuta de manera automatica son los metodos: __enter__ y __exit__
# __enter__ abre el archivo y __exit__ lo cierra


#video 12 clase 2:
#importamos la clase del video 11
from ManejoArchivos import ManejoArchivos

with ManejoArchivos('prueba.txt') as archivo:
    print(archivo.read())
