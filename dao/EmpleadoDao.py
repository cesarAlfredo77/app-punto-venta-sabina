from util.ConexionBd import ConexionBd

class EmpleadoDao:
    def __init__(self) -> None:
        self.conexion = ConexionBd().getConexionBd()

    def listarEmpleados(self):
        cursor = self.conexion.cursor()
        sql = "SELECT e.idempleado, p.nombres, e.area, e.puesto, e.correoEmpresa, e.sueldo FROM empleado e INNER JOIN persona p ON e.idpersona = p.idpersona"
        cursor.execute(sql)
        return cursor.fetchall()
    
    def buscarEmpleado(self, idEmpleado):
        cursor = self.conexion.cursor()
        sql = "SELECT e.idempleado, p.nombres, e.area, e.puesto, e.correoEmpresa, e.sueldo FROM empleado e INNER JOIN persona p ON e.idpersona = p.idpersona WHERE e.idempleado = '{}'".format(
            idEmpleado)
        cursor.execute(sql)
        return cursor.fetchone()
    
    def insertarEmpleado(self, empleado):
        cursor = self.conexion.cursor()
        sql = "INSERT INTO empleado ( idEmpleado, idPersona, area, puesto, correoEmpresa, sueldo) VALUES ('{}', '{}', '{}', '{}', '{}', '{}')".format(
            empleado.get_idEmpleado(), empleado.get_idPersona(), empleado.get_area(), empleado.get_puesto(), empleado.get_correoEmpresa(), empleado.get_sueldo())
        cursor.execute(sql)
        self.conexion.commit()
        cursor.close()
    
    def actualizarEmpleado(self, empleado):
        cursor = self.conexion.cursor()
        sql = "UPDATE empleado SET idPersona = '{}', area = '{}', puesto = '{}', correoEmpresa = '{}', sueldo = '{}' where idEmpleado = '{}'".format(
           empleado.get_idPersona(), empleado.get_area(), empleado.get_puesto(), empleado.get_correoEmpresa(), empleado.get_sueldo(), empleado.get_idEmpleado())
        cursor.execute(sql)
        self.conexion.commit()
        cursor.close()

    def listarPersona(self):
        cursor = self.conexion.cursor()
        sql = "SELECT idPersona, tipoDoc, numDoc, nombres, apellidos, fechaNac, telefono, correo, direccion FROM persona"
        cursor.execute(sql)
        return cursor.fetchall()