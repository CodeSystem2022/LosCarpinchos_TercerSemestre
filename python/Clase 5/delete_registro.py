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
            sentencia = 'DELETE FROM persona WHERE id_persona=%s' # no olvidarse del WHERE
            entrada = input('Digite el nro de registro a eliminar: ')
            # valores = (7,)  # tupla de valores
            valores = (entrada,)
            cursor.execute(sentencia, valores) # sentencia para varios registros
            registros_eliminados = cursor.rowcount
            print(f'los registros eliminados son: {registros_eliminados}')


except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()

