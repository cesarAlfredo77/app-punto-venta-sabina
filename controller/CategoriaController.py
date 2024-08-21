from PyQt5 import QtWidgets, uic
from dao.CategoriaDao import CategoriaDao
from PyQt5.QtWidgets import QTableWidgetItem
from model.Categoria import Categoria

class CategoriaController:

    def __init__(self):
        #app = QtWidgets.QApplication([])
        self.objCategoriaDao = CategoriaDao()
        self.ventana = uic.loadUi("view/frmcategoria.ui")
        self.listarCategorias()
        self.listarEstado()
        self.ventana.tblcategorias.cellClicked.connect(self.tblCategoriasCellClick)
        self.ventana.btnnuevo.clicked.connect(self.nuevoFormularioCategoria)
        self.ventana.btnguardar.clicked.connect(self.btnGuardarCategoriaClick)
        self.ventana.btnsalir.clicked.connect(self.cerrarVentana)
        #self.ventana.show()
        #app.exec()
  


    def nuevoFormularioCategoria(self):
        self.ventana.txtidcategoria.setText("")
        self.ventana.txtidcategoria.setEnabled(True)
        self.ventana.txtnombre.setText("")
        self.ventana.txtdescripcion.setText("")
        self.ventana.cboestado.setCurrentIndex(0)        
    
    def tblCategoriasCellClick(self, fila):
        codCategoria = self.ventana.tblcategorias.item(fila, 0).text()
        self.ventana.txtidcategoria.setText(codCategoria)
        self.ventana.txtidcategoria.setEnabled(False)
        objCategoria = self.objCategoriaDao.buscarCategoria(codCategoria)
        self.ventana.txtnombre.setText(objCategoria[1])
        self.ventana.txtdescripcion.setText(objCategoria[2])
        self.ventana.cboestado.setCurrentText(objCategoria[3])  

    def btnGuardarCategoriaClick(self):
        idcategoria = self.ventana.txtidcategoria.text()
        nombre = self.ventana.txtnombre.text()
        descripcion = self.ventana.txtdescripcion.text()
        estado = self.ventana.cboestado.currentText()        
        nuevaCategoria = Categoria(idcategoria, nombre, descripcion, estado)
        if self.ventana.txtidcategoria.isEnabled():
            self.objCategoriaDao.insertarCategoria(nuevaCategoria)
        else:
            self.objCategoriaDao.actualizarCategoria(nuevaCategoria)
        self.listarCategorias()   

    def listarCategorias(self):
        listCategorias = self.objCategoriaDao.listarCategorias()
        cantidad = len(listCategorias)
        self.ventana.tblcategorias.setRowCount(cantidad)
        fila = 0
        for objCategoria in listCategorias:
            self.ventana.tblcategorias.setItem(fila, 0, QTableWidgetItem(objCategoria[0]))
            self.ventana.tblcategorias.setItem(fila, 1, QTableWidgetItem(objCategoria[1]))
            self.ventana.tblcategorias.setItem(fila, 2, QTableWidgetItem(objCategoria[2]))
            self.ventana.tblcategorias.setItem(fila, 3, QTableWidgetItem(objCategoria[3]))

            fila +=1

    def listarEstado(self):        
        self.ventana.cboestado.addItem("ACTIVO")
        self.ventana.cboestado.addItem("INACTIVO")
    
    def cerrarVentana(self):
        self.ventana.close()

