from NumerosIgualesExcepcion import NumerosIgualesExcepcion


resultado = None    # variable global
#a = 7
#b= 0


try:        #bloque
    a = int(input('digite el primer numero: '))
    b = int(input('digite el segundo numero: '))

    if a == b:
        raise NumerosIgualesExcepcion('los numeros son iguales ')  # palabra para arrojar un tipo de excepcion

    resultado = a / b    # no se modifica el valor
except TypeError as e:
    print(f'TypeError - ocurrio un error: {type(e)}')
except ZeroDivisionError as e:
    print(f'ZeroDivisionError - ocurrio un error: {type(e)}')
except Exception as e:      # capturamos el error generico - ZeroDivisionError especifico
    print (f'Exception - ocurrio un error: {type(e)}')

else:
    print("no se arrojo ninguna excepcion")


finally:        # siempre se va a ejecutar
    print("ejecucion de este bloque finally")

print(f'el resultado es: {resultado}')
print('seguimos...')
