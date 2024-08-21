from util.ConexionBd import ConexionBd

class GrupoClienteDao:

    def __init__(self):
        self.conexion = ConexionBd().getConexionBd()
    
    def listarGrupoCliente(self):
        cursor = self.conexion.cursor()
        sql = "select idgrupocli, nombre, beneficio, estado from grupocliente order by idgrupocli asc"
        cursor.execute(sql)
        return cursor.fetchall()
    
    def buscarGrupoCliente(self, codgrupocliente):
        cursor = self.conexion.cursor()
        sql = "select idgrupocli, nombre, beneficio, estado from grupocliente where idgrupocli = '{}'".format(codgrupocliente)
        cursor.execute(sql)
        return cursor.fetchone()
    
    def insertarGrupoCliente(self, grupocliente):
        cursor = self.conexion.cursor()
        sql = "INSERT INTO grupocliente VALUES ('{}','{}', '{}', '{}')".format(grupocliente.idgrupocli, grupocliente.nombre, grupocliente.beneficio, grupocliente.estado)
        cursor.execute(sql)
        self.conexion.commit()
        cursor.close()
    
    def actualizarGrupoCliente(self, grupocliente):
        cursor = self.conexion.cursor()
        sql = "update grupocliente SET nombre = '{}', beneficio = '{}', estado = '{}' where idgrupocli = '{}'".format(grupocliente.nombre, grupocliente.beneficio, grupocliente.estado, grupocliente.idgrupocli)
        cursor.execute(sql)
        self.conexion.commit()
        cursor.close()


