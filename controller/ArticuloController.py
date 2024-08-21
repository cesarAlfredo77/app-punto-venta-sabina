from PyQt5 import QtWidgets, uic
from dao.ArticuloDao import ArticuloDao
from PyQt5.QtWidgets import QTableWidgetItem
from model.Articulo import Articulo

class ArticuloController:

    def __init__(self):
        #app = QtWidgets.QApplication([])
        self.ventana = uic.loadUi("view/frmarticulo.ui")
        self.articuloDao = ArticuloDao()
        self.listarArticulos()
        self.listarCategoria()
        self.listarUndMedida()
        self.listarEstado()
        self.ventana.tblarticulos.cellClicked.connect(self.tblArticulosCellClick)
        self.ventana.btnnuevo.clicked.connect(self.nuevoFormularioArticulo)
        self.ventana.btnguardar.clicked.connect(self.btnGuardarArticuloClick)
        self.ventana.btnsalir.clicked.connect(self.cerrarVentana)
        #self.ventana.show()
        #app.exec()
    
    def btnGuardarArticuloClick(self):
        idarticulo = self.ventana.txtidarticulo.text()
        idcategoria = self.ventana.cboidcategoria.currentData()
        codigo = self.ventana.txtcodigo.text()
        descripcion = self.ventana.txtdescripcion.text()
        und_medida = self.ventana.cboundmedida.currentText()
        stock = self.ventana.txtstock.text()
        estado = self.ventana.cboestado.currentText()    
        nuevoArticulo = Articulo(idarticulo, idcategoria, codigo, descripcion, und_medida, stock, estado)
        if self.ventana.txtidarticulo.isEnabled():
            self.articuloDao.insertarArticulo(nuevoArticulo)
        else:
            self.articuloDao.actualizarArticulo(nuevoArticulo)
        self.listarArticulos()     

    
    def nuevoFormularioArticulo(self):
        self.ventana.txtidarticulo.setText("")
        self.ventana.txtidarticulo.setEnabled(True)
        self.ventana.cboidcategoria.setCurrentIndex(0)
        self.ventana.txtcodigo.setText("")
        self.ventana.txtcodigo.setEnabled(True)
        self.ventana.txtdescripcion.setText("")
        self.ventana.cboundmedida.setCurrentIndex(0)
        self.ventana.txtstock.setText("")
        self.ventana.cboestado.setCurrentIndex(0)        
    
    def tblArticulosCellClick(self, fila):
        codArticulo = self.ventana.tblarticulos.item(fila, 0).text()
        self.ventana.txtidarticulo.setText(codArticulo)
        self.ventana.txtidarticulo.setEnabled(False)
        objArticulo = self.articuloDao.buscarArticulo(codArticulo)
        self.ventana.cboidcategoria.setCurrentText(objArticulo[1])
        self.ventana.txtcodigo.setText(objArticulo[2])
        self.ventana.txtcodigo.setEnabled(False)
        self.ventana.txtdescripcion.setText(objArticulo[3])
        self.ventana.cboundmedida.setCurrentText(objArticulo[4])
        self.ventana.txtstock.setText(str(objArticulo[5]))
        self.ventana.cboestado.setCurrentText(objArticulo[6]) 

    def listarArticulos(self):
        listArticulos = self.articuloDao.listarArticulos()
        cantidad = len(listArticulos)
        self.ventana.tblarticulos.setRowCount(cantidad)
        fila = 0
        for objArticulo in listArticulos:
            self.ventana.tblarticulos.setItem(fila, 0, QTableWidgetItem(objArticulo[0]))
            self.ventana.tblarticulos.setItem(fila, 1, QTableWidgetItem(objArticulo[1]))
            self.ventana.tblarticulos.setItem(fila, 2, QTableWidgetItem(objArticulo[2]))
            self.ventana.tblarticulos.setItem(fila, 3, QTableWidgetItem(objArticulo[3]))
            self.ventana.tblarticulos.setItem(fila, 4, QTableWidgetItem(objArticulo[4]))
            self.ventana.tblarticulos.setItem(fila, 5, QTableWidgetItem(str(objArticulo[5])))
            self.ventana.tblarticulos.setItem(fila, 6, QTableWidgetItem(objArticulo[6]))
            fila +=1

    def listarCategoria(self):
        listCategoria = self.articuloDao.listarCategoria()
        for objCategoria in listCategoria:
            self.ventana.cboidcategoria.addItem(objCategoria[1], objCategoria[0])

    def listarUndMedida(self):        
        self.ventana.cboundmedida.addItem("Kg")
        self.ventana.cboundmedida.addItem("Lt")
        self.ventana.cboundmedida.addItem("Und")
    
    def listarEstado(self):        
        self.ventana.cboestado.addItem("ACTIVO")
        self.ventana.cboestado.addItem("INACTIVO")
    
    def cerrarVentana(self):
        self.ventana.close()
