import mysql.connector

class ConexionBd():
    def __init__(self):
        self.conexion = mysql.connector.connect(host='localhost', database='punto_venta_sabina', user='root', password='root245')
    
    def getConexionBd(self):
        return self.conexion
    