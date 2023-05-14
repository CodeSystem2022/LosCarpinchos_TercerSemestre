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
            sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
            valores = (
                ('Juan', 'Perez', 'jperez@mail.com', 4),
                ('Rocio', 'Ayala', 'ayalar@mail.com', 5)
            ) # una tupla de tupla
            cursor.executemany(sentencia, valores) # sentencia para varios registros
            registros_actualizados = cursor.rowcount
            print(f'los registros actualizados son: {registros_actualizados}')


except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()

