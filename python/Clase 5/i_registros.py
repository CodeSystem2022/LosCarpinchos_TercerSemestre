
import psycopg2
# conectanmos al Postgre


conexion = psycopg2.connect(
    user='postgres',
    password='Admin',
    host='127.0.0.1',
    port='5432',
    database='test_bd'
)


try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO persona (nombre, apellido, email) VALUES (%s, %s, %s)'
            valores = ('Carlos', 'Lara', 'clara@mail.com')  # es una tupla
            cursor.execute(sentencia, valores)
            # conexion.comit()  # se utiliza para guardar los cambios en la BD
            registros_insertados = cursor.rowcount
            print(f'los registros insertados son: {registros_insertados}')


except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()

