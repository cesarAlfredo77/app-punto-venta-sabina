from PyQt5 import QtWidgets, uic
from dao.EmpleadoDao import EmpleadoDao
from PyQt5.QtWidgets import QTableWidgetItem
from model.Empleado import Empleado

class EmpleadoController:

    def __init__(self):
        #app = QtWidgets.QApplication([])
        self.ventana  = uic.loadUi("view/frmempleado.ui")
        self.empleadoDao = EmpleadoDao()
        self.listarEmpleados()
        self.listarPersona()
        self.listarArea()
        self.listarPuesto()
        self.ventana.tblempleado.cellClicked.connect(self.tblempleadoCellClick)
        self.ventana.btnguardar.clicked.connect(self.btnguardarEmpleadoClick)
        self.ventana.btnnuevo.clicked.connect(self.btnnuevoOnClick)
        self.ventana.btnsalir.clicked.connect(self.btnsalirOnClick)
        #self.ventana.show()
        #app.exec()

    def btnguardarEmpleadoClick(self):
        idEmpleado = self.ventana.txtidempleado.text()
        idPersona = self.ventana.cboidpersona.currentData()
        area = self.ventana.cboarea.currentText()
        puesto = self.ventana.cbopuesto.currentText()
        correoEmpresa = self.ventana.txtcorreoempresa.text()
        sueldo = self.ventana.txtsueldo.text()
        nuevoEmpleado = Empleado (idEmpleado, idPersona, area, puesto, correoEmpresa, sueldo)
        if self.ventana.txtidempleado.isEnabled():
            self.empleadoDao.insertarEmpleado(nuevoEmpleado)
        else:
            self.empleadoDao.actualizarEmpleado(nuevoEmpleado)
        self.listarEmpleados()
    
    def btnnuevoOnClick(self):
        self.ventana.txtidempleado.setText("")
        self.ventana.txtidempleado.setEnabled(True)
        self.ventana.cboidpersona.setCurrentIndex(0)
        self.ventana.cboarea.setCurrentIndex(0)
        self.ventana.cbopuesto.setCurrentIndex(0)
        self.ventana.txtcorreoempresa.setText("")
        self.ventana.txtsueldo.setText("")

    def btnsalirOnClick(self):
        self.ventana.close()

    def tblempleadoCellClick(self, fila):
        idEmpleado = self.ventana.tblempleado.item(fila, 0).text()
        self.ventana.txtidempleado.setText(idEmpleado)
        self.ventana.txtidempleado.setEnabled(False)
        objEmpleado = self.empleadoDao.buscarEmpleado(idEmpleado)
        self.ventana.cboidpersona.setCurrentText(objEmpleado[1])
        self.ventana.cboarea.setCurrentText(objEmpleado[2])
        self.ventana.cbopuesto.setCurrentText(objEmpleado[3])
        self.ventana.txtcorreoempresa.setText(objEmpleado[4])
        self.ventana.txtsueldo.setText(str(objEmpleado[5]))

    def listarEmpleados(self):
        listEmpleados = self.empleadoDao.listarEmpleados()
        cantidad = len(listEmpleados)
        self.ventana.tblempleado.setRowCount(cantidad)
        fila = 0
        for objEmpleado in listEmpleados:
            self.ventana.tblempleado.setItem(fila, 0, QTableWidgetItem(objEmpleado[0]))
            self.ventana.tblempleado.setItem(fila, 1, QTableWidgetItem(objEmpleado[1]))
            self.ventana.tblempleado.setItem(fila, 2, QTableWidgetItem(objEmpleado[2]))
            self.ventana.tblempleado.setItem(fila, 3, QTableWidgetItem(objEmpleado[3]))
            self.ventana.tblempleado.setItem(fila, 4, QTableWidgetItem(objEmpleado[4]))
            self.ventana.tblempleado.setItem(fila, 5, QTableWidgetItem(str(objEmpleado[5])))
            fila +=1

    def listarPersona(self):
        listPersona = self.empleadoDao.listarPersona()
        for objPersona in listPersona:
            self.ventana.cboidpersona.addItem(objPersona[3], objPersona[0])

    def listarArea(self):
        self.ventana.cboarea.addItem("VENTA")
        self.ventana.cboarea.addItem("GERENCIA")
        self.ventana.cboarea.addItem("ALMACÉN")

    def listarPuesto(self):
        self.ventana.cbopuesto.addItem("GERENTE")
        self.ventana.cbopuesto.addItem("CAJERO")
        self.ventana.cbopuesto.addItem("VENDEDOR")
        self.ventana.cbopuesto.addItem("ALMACENERO")