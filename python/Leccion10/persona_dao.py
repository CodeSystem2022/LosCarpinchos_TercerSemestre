from capa_dato_persona.Persona import Persona
from capa_dato_persona.conexion import Conexion
from logger_base import log


class PersonaDAO:
    '''
    DAO significa Data Access Object
    CRUS significa:
                   Create -> Insertar
                   Read -> Seleccionar
                   Update -> Actualizar
                   Delete -> Eliminar
    '''
    _SELECCIONAR = 'SELCT * FROM persona ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO peersona(nombre, apellido, email) VALUES(%s, %s, %s)'
    _ACTUALIZAR = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    _ELIMINAR = 'DELETE FROM persona WHERE id_persona=%s'

    #Definimos los métodos de clase
    @classmethod
    def seleccionar(cls):
        #with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                personas = [] #Creamos una lista
                for registro in registros:
                    persona = Persona(registro[0], registro[1], registro[2], registro[3])
                    personas.append(persona)
                return personas

    @classmethod
    def insertar(cls, persona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (persona.nombre, persona.apellido, persona.email)
                cursor.execute(cls._INSERTAR, valores)
                log.debug(f'Persona Insertada: {persona}')
                return cursor.rowcount

    @classmethod
    def actualizar(cls, persona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores =(persona.nombre, persona.apellido, persona.email, persona.id_persona)
                cursor.execute(cls._ACTUALIZAR, valores)
                log.debug(f'Persona actualizada: {persona}')
                return cursor.rowcount

    @classmethod
    def eliminar(cls, persona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (persona.id_persona,)
                cursor.execute(cls._ELIMINAR, valores)
                log.debug(f'Los objetos eliminados son: {persona}')
                return cursor.rowcount

if __name__== '__main__':

    #Eliminar un registro
    persona1 = Persona(id_persona=8)
    personas_eliminadas = PersonaDAO.eliminar(persona1)
    log.debug(f'Personas eliminadas: {personas_eliminadas}')

    # Actualizar un registro
    #persona1 = Persona(1, 'Juan José', 'Pena', ' jjpen@mail.com')
    #personas_actualizadas = PersonaDAO.actualizar(persona1)
    #log.debug(f'Personasactualizadas: {personas_actualizadas}')

    #Insertar un registro
    #persona1 = Persona(nombre= 'Omero', apellido='Ramos', email='omeror@mail.com')
    #personas_insertadas= PersonaDAO.insertar(persona1)
    #log.debug(f'Personas Insertadas: {personas_insertadas}')

    #Seleccionar objeto
    personas = PersonaDAO.seleccionar()
    for persona in personas:
        log.debug(persona)
