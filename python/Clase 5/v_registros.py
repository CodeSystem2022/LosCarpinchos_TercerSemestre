
import psycopg2
# conectanmos al Postgre


conexion = psycopg2.connect(
    user='postgres',
    password='Admin',
    host='127.0.0.1',
    port='5432',
    database='test_bd'
)


"""
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'SELECT * FROM persona WHERE id_persona IN (1, 2, 3)' # placeholder
            # id_persona = input('Digite un numero para el id_persona: ')
            cursor.execute(sentencia)
            registros = cursor.fetchall()
            for registro in registros:
                print(registro)

except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()

"""


try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'SELECT * FROM persona WHERE id_persona IN %s'
            entrada = input('Digite los id_persona a buscar (separados por comas): ')
            llaves_primarias = (tuple(entrada.split(', ')),)
            cursor.execute(sentencia, llaves_primarias)
            registros = cursor.fetchall()
            for registro in registros:
                print(registro)

except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()

