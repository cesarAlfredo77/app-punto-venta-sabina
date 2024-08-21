from PyQt5 import QtWidgets, uic
from dao.GrupoClienteDao import GrupoClienteDao
from PyQt5.QtWidgets import QTableWidgetItem
from model.GrupoCliente import GrupoCliente

class GrupoClienteController:

    def __init__(self):
        #app = QtWidgets.QApplication([])
        self.objGrupoClienteDao = GrupoClienteDao()
        self.ventana = uic.loadUi("view/frmgrupocliente.ui")
        self.listarGrupoCliente()
        self.listarBeneficio()
        self.listarEstado()
        self.ventana.tblgrupocliente.cellClicked.connect(self.tblgrupoclienteCellClick)
        self.ventana.btnnuevo.clicked.connect(self.nuevoFormularioGrupoCliente)
        self.ventana.btnguardar.clicked.connect(self.btnGuardarGrupoClienteClick)
        self.ventana.btnsalir.clicked.connect(self.cerrarVentana)
        #self.ventana.show()
        #app.exec()
  


    def nuevoFormularioGrupoCliente(self):
        self.ventana.txtidgrupocli.setText("")
        self.ventana.txtidgrupocli.setEnabled(True)
        self.ventana.txtnombre.setText("")
        self.ventana.cbobeneficio.setCurrentIndex(0)   
        self.ventana.cboestado.setCurrentIndex(0)        
    
    def tblgrupoclienteCellClick(self, fila):
        codGrupoCli = self.ventana.tblgrupocliente.item(fila, 0).text()
        self.ventana.txtidgrupocli.setText(codGrupoCli)
        self.ventana.txtidgrupocli.setEnabled(False)
        objGrupoCli = self.objGrupoClienteDao.buscarGrupoCliente(codGrupoCli)
        self.ventana.txtnombre.setText(objGrupoCli[1])
        self.ventana.cbobeneficio.setCurrentText(objGrupoCli[2])
        self.ventana.cboestado.setCurrentText(objGrupoCli[3])  

    def btnGuardarGrupoClienteClick(self):
        idgrupocli = self.ventana.txtidgrupocli.text()
        nombre = self.ventana.txtnombre.text()
        beneficio = self.ventana.cbobeneficio.currentText()  
        estado = self.ventana.cboestado.currentText()        
        nuevoGrupoCli = GrupoCliente(idgrupocli, nombre, beneficio, estado)
        if self.ventana.txtidgrupocli.isEnabled():
            self.objGrupoClienteDao.insertarGrupoCliente(nuevoGrupoCli)
        else:
            self.objGrupoClienteDao.actualizarGrupoCliente(nuevoGrupoCli)
        self.listarGrupoCliente()   

    def listarGrupoCliente(self):
        listGrupocli = self.objGrupoClienteDao.listarGrupoCliente()
        cantidad = len(listGrupocli)
        self.ventana.tblgrupocliente.setRowCount(cantidad)
        fila = 0
        for objGrupoCli in listGrupocli:
            self.ventana.tblgrupocliente.setItem(fila, 0, QTableWidgetItem(objGrupoCli[0]))
            self.ventana.tblgrupocliente.setItem(fila, 1, QTableWidgetItem(objGrupoCli[1]))
            self.ventana.tblgrupocliente.setItem(fila, 2, QTableWidgetItem(objGrupoCli[2]))
            self.ventana.tblgrupocliente.setItem(fila, 3, QTableWidgetItem(objGrupoCli[3]))

            fila +=1

    def listarBeneficio(self):        
        self.ventana.cbobeneficio.addItem("DESCUENTO 50%")
        self.ventana.cbobeneficio.addItem("DESCUENTO 20%")
        self.ventana.cbobeneficio.addItem("DESCUENTO 10%")

    def listarEstado(self):        
        self.ventana.cboestado.addItem("ACTIVO")
        self.ventana.cboestado.addItem("INACTIVO")
    
    def cerrarVentana(self):
        self.ventana.close()

