from util.ConexionBd import ConexionBd

class CategoriaDao:

    def __init__(self):
        self.conexion = ConexionBd().getConexionBd()
    
    def listarCategorias(self):
        cursor = self.conexion.cursor()
        sql = "select idcategoria, nombre, descripcion, estado from categoria order by idcategoria asc"
        cursor.execute(sql)
        return cursor.fetchall()
    
    def buscarCategoria(self, codcategoria):
        cursor = self.conexion.cursor()
        sql = "select idcategoria, nombre, descripcion, estado from categoria where idcategoria = '{}'".format(codcategoria)
        cursor.execute(sql)
        return cursor.fetchone()
    
    def insertarCategoria(self, categoria):
        cursor = self.conexion.cursor()
        sql = "INSERT INTO categoria VALUES ('{}','{}', '{}', '{}')".format(categoria.idcategoria, categoria.nombre, categoria.descripcion, categoria.estado)
        cursor.execute(sql)
        self.conexion.commit()
        cursor.close()
    
    def actualizarCategoria(self, categoria):
        cursor = self.conexion.cursor()
        sql = "update categoria SET nombre = '{}', descripcion = '{}', estado = '{}' where idcategoria = '{}'".format(categoria.nombre, categoria.descripcion, categoria.estado, categoria.idcategoria)
        cursor.execute(sql)
        self.conexion.commit()
        cursor.close()


