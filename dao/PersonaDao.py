from util.ConexionBd import ConexionBd

class PersonaDao:

    def __init__(self):
        self.conexion = ConexionBd().getConexionBd()

    def listarPersonas(self):
        cursor = self.conexion.cursor()
        sql = "SELECT idPersona, tipoDoc, numDoc, nombres, apellidos, fechaNac, telefono, correo, direccion FROM persona order by idPersona DESC"
        cursor.execute(sql)
        return cursor.fetchall()
    
    def buscarPersona(self, idPersona):
        cursor = self.conexion.cursor()
        sql = "SELECT idPersona, tipoDoc, numDoc, nombres, apellidos, fechaNac, telefono, correo, direccion FROM persona WHERE idPersona = '{}' ".format(
            idPersona)
        cursor.execute(sql)
        return cursor.fetchone()
    
    def insertarPersona(self, persona):
        cursor = self.conexion.cursor()
        sql = "INSERT INTO persona (idPersona, tipoDoc, numDoc, nombres, apellidos, fechaNac, telefono, correo, direccion) VALUES ( '{}' , '{}' , '{}' , '{}' , '{}' , '{}' , '{}' , '{}' , '{}')".format(
            persona.get_idPersona(), persona.get_tipoDoc(), persona.get_numDoc(), persona.get_nombres(), persona.get_apellidos(), persona.get_fechaNac(), persona.get_telefono(), persona.get_correo(), persona.get_direccion())
        cursor.execute(sql)
        self.conexion.commit()
        cursor.close()
    
    def actualizarPersona(self, persona):
        cursor = self.conexion.cursor()
        sql = " UPDATE persona SET tipoDoc = '{}' , numDoc = '{}' , nombres = '{}' , apellidos = '{}' , fechaNac = '{}' , telefono = '{}' , correo = '{}' , direccion = '{}' where idPersona = '{}' ".format(
            persona.get_tipoDoc(), persona.get_numDoc(), persona.get_nombres(), persona.get_apellidos(), persona.get_fechaNac(), persona.get_telefono(), persona.get_correo(), persona.get_direccion(),  persona.get_idPersona())
        cursor.execute(sql)
        self.conexion.commit()
        cursor.close()