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
            sentencia = 'DELETE FROM persona WHERE id_persona IN %s'  # eliminar varios reg
            entrada = input('Digite los nro de registros a eliminar (separados por coma): ')
            valores = (tuple(entrada.split(',')),)  #tupla de tuplas
            cursor.execute(sentencia, valores)
            registros_eliminados = cursor.rowcount
            print(f'los registros eliminados son: {registros_eliminados}')


except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()

