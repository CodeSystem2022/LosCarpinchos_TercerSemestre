class ManejoArchivos: #creamos clase
    def __init__(self, nombre): #creamos metodo
        self.nombre = nombre

    def __enter__(self):
        print('Obtenemos el recurso'.center(50, '-'))
        self.nombre = open(self.nombre, 'r', encoding='utf-8') #encapsulamos el codigodentro del metodo
        return self.nombre

    def __exit__(self, exception_type, exc_value, traza_error): #se puede cambiar los nombres de los parametros
        print('cerramos el recurso'.center(50, '-'))
        if self.nombre: #si nombre es verdadero...
            self.nombre.close() #cerramos el archivo
