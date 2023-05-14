
import psycopg2
# conectanmos al Postgre


conexion = psycopg2.connect(
    user='postgres',
    password='Admin',
    host='127.0.0.1',
    port='5432',
    database='test_bd'
)

#print(conexion)   # conexion a la base de dato

"""try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'SELECT * FROM persona'
            cursor.execute(sentencia)    # de esta manera ejecutamos la sentencia
            registros = cursor.fetchall()   # recuperamos todos los registros que seran una lista
            print(registros) # listas internamente tuplas

except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()
"""

# sin el with debemos usar
# cursor = conexion.cursor()
# cursor.close()
# con el with  #  cierra el cursor


# cambios en la sentencia

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'SELECT * FROM persona WHERE id_persona = %s' # placeholder
            id_persona = input('Digite un numero para el id_persona: ')
            cursor.execute(sentencia, (id_persona, ))  # tupla
            registros = cursor.fetchone()  # apunta a la tupla
            print(registros)

except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()




#  https://www.psycopg.org/docs/usage.html - with statement¶