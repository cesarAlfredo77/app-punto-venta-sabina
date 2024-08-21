from util.ConexionBd import ConexionBd

class ArticuloDao:

    def __init__(self) -> None:
        self.conexion = ConexionBd().getConexionBd()

    def listarArticulos(self):
        cursor = self.conexion.cursor()
        sql = "SELECT a.idarticulo, c.nombre, a.codigo, a.descripcion, a.und_medida, a.stock, a.estado FROM articulo a INNER JOIN categoria c ON a.idcategoria = c.idcategoria"
        cursor.execute(sql)
        return cursor.fetchall()
    
    def buscarArticulo(self, idarticulo):
        cursor = self.conexion.cursor()
        sql = "SELECT a.idarticulo, c.nombre, a.codigo, a.descripcion, a.und_medida, a.stock, a.estado FROM articulo a INNER JOIN categoria c ON a.idcategoria = c.idcategoria WHERE a.idarticulo = '{}'".format(idarticulo)
        cursor.execute(sql)
        return cursor.fetchone()
    
    def insertarArticulo(self, articulo):
        cursor = self.conexion.cursor()
        sql = "INSERT INTO articulo (idarticulo, idcategoria, codigo, descripcion, und_medida, stock, estado) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(articulo.idarticulo, articulo.idcategoria, articulo.codigo, articulo.descripcion, articulo.und_medida, articulo.stock, articulo.estado)
        cursor.execute(sql)
        self.conexion.commit()
        cursor.close()
    
    def actualizarArticulo(self, articulo):
        cursor = self.conexion.cursor()
        sql = "UPDATE articulo SET idcategoria = '{}', codigo = '{}', descripcion = '{}', und_medida = '{}', stock = '{}', estado = '{}' where idarticulo = '{}'".format(
            articulo.idcategoria, articulo.codigo, articulo.descripcion, articulo.und_medida, articulo.stock, articulo.estado, articulo.idarticulo)
        cursor.execute(sql)
        self.conexion.commit()
        cursor.close()

    def listarCategoria(self):
        cursor = self.conexion.cursor()
        sql = "SELECT idcategoria, nombre, descripcion, estado FROM categoria"
        cursor.execute(sql)
        return cursor.fetchall()