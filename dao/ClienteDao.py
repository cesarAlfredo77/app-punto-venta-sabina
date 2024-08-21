from util.ConexionBd import ConexionBd

class ClienteDao:

    def __init__(self) -> None:
        self.conexion = ConexionBd().getConexionBd()

    def listarClientes(self):
        cursor = self.conexion.cursor()
        sql = "SELECT c.idcliente, g.nombre, c.codcliente, c.estcontribuyente, c.condcontribuyente, c.lineacredito, c.condpago, p.nombres FROM cliente c INNER JOIN grupocliente g ON c.idgrupocli = g.idgrupocli INNER JOIN persona p ON c.idpersona = p.idpersona"
        cursor.execute(sql)
        return cursor.fetchall()
    
    def buscarCliente(self, idcliente):
        cursor = self.conexion.cursor()
        sql = "SELECT c.idcliente, g.nombre, c.codcliente, c.estcontribuyente, c.condcontribuyente, c.lineacredito, c.condpago, p.nombres FROM cliente c INNER JOIN grupocliente g ON c.idgrupocli = g.idgrupocli INNER JOIN persona p ON c.idpersona = p.idpersona WHERE c.idcliente = '{}'".format(idcliente)
        cursor.execute(sql)
        return cursor.fetchone()
    
    def insertarCliente(self, cliente):
        cursor = self.conexion.cursor()
        sql = "INSERT INTO cliente (idcliente, idgrupocli, codcliente, estcontribuyente, condcontribuyente, lineacredito, condpago, idpersona) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(cliente.idcliente, cliente.idgrupocli, cliente.codcliente, cliente.estcontribuyente, cliente.condcontribuyente, cliente.lineacredito, cliente.condpago, cliente.idpersona)
        cursor.execute(sql)
        self.conexion.commit()
        cursor.close()
    
    def actualizarCliente(self, cliente):
        cursor = self.conexion.cursor()
        sql = "UPDATE cliente SET idgrupocli = '{}', codcliente = '{}', estcontribuyente = '{}', condcontribuyente = '{}', lineacredito = '{}', condpago = '{}', condpago = '{}' where idarticulo = '{}'".format(
            cliente.idcategoria, cliente.codigo, cliente.descripcion, cliente.und_medida, cliente.stock, cliente.estado, cliente.idarticulo)
        cursor.execute(sql)
        self.conexion.commit()
        cursor.close()

    def listarCliente(self):
        cursor = self.conexion.cursor()
        sql = "SELECT idcategoria, nombre, descripcion, estado FROM categoria"
        cursor.execute(sql)
        return cursor.fetchall()