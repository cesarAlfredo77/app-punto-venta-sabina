from PyQt5 import QtWidgets, uic
from dao.PersonaDao import PersonaDao
from model.Persona import Persona
from PyQt5.QtWidgets import QTableWidgetItem

class PersonaController:
    
    def __init__(self):
        #app = QtWidgets.QApplication([])
        self.ventana = uic.loadUi("view/frmpersona.ui")
        self.PersonaDao = PersonaDao()
        self.ventana.tblpersona.cellClicked.connect(self.tblpersonaCellClick)
        self.ventana.btnguardar.clicked.connect(self.btnguardarPersonaClick)
        self.ventana.btnnuevo.clicked.connect(self.btnnuevoOnClick)
        self.ventana.btnsalir.clicked.connect(self.btnsalirOnClick)
        self.ventana.show()
        self.listarPersonas()
        self.listarDocumentos()
        #app.exec()

    def btnguardarPersonaClick(self):
        idPersona = self.ventana.txtidpersona.text()
        tipoDoc = self.ventana.cbotipodocumento.currentText()
        numDoc = self.ventana.txtnumdocumento.text()
        nombres = self.ventana.txtnombres.text()
        apellidos = self.ventana.txtapellidos.text()
        fechaNac = self.ventana.txtfecha.text()
        telefono = self.ventana.txttelefono.text()
        correo = self.ventana.txtcorreo.text()
        direccion = self.ventana.txtdireccion.text()
        nuevaPersona = Persona(idPersona, tipoDoc, numDoc, nombres, apellidos, fechaNac, telefono, correo, direccion)
        if self.ventana.txtidpersona.isEnabled():
            self.PersonaDao.insertarPersona(nuevaPersona)
        else:
            self.PersonaDao.actualizarPersona(nuevaPersona)
        self.listarPersonas()

    def btnnuevoOnClick(self):
        self.ventana.txtidpersona.setText("")
        self.ventana.txtidpersona.setEnabled(True)
        self.ventana.cbotipodocumento.setCurrentIndex(0)
        self.ventana.txtnumdocumento.setText("")
        self.ventana.txtnombres.setText("")
        self.ventana.txtapellidos.setText("")
        self.ventana.txtfecha.setText("")
        self.ventana.txttelefono.setText("")
        self.ventana.txtcorreo.setText("")
        self.ventana.txtdireccion.setText("")

    def btnsalirOnClick(self):
        self.ventana.close()

    def tblpersonaCellClick(self, fila):
        idPersona = self.ventana.tblpersona.item(fila, 0).text()
        self.ventana.txtidpersona.setText(idPersona)
        self.ventana.txtidpersona.setEnabled(False)
        objPersona = self.PersonaDao.buscarPersona(idPersona)
        self.ventana.cbotipodocumento.setCurrentText(objPersona[1])
        self.ventana.txtnumdocumento.setText(objPersona[2])
        self.ventana.txtnombres.setText(objPersona[3])
        self.ventana.txtapellidos.setText(objPersona[4])
        self.ventana.txtfecha.setText(objPersona[5])
        self.ventana.txttelefono.setText(objPersona[6])
        self.ventana.txtcorreo.setText(objPersona[7])
        self.ventana.txtdireccion.setText(objPersona[8])

    def listarPersonas(self):
        listPersonas = self.PersonaDao.listarPersonas()
        cantidad = len(listPersonas)
        self.ventana.tblpersona.setRowCount(cantidad)
        fila = 0
        for objPersona in listPersonas:
            self.ventana.tblpersona.setItem(fila, 0, QTableWidgetItem(objPersona[0]))
            self.ventana.tblpersona.setItem(fila, 1, QTableWidgetItem(objPersona[1]))
            self.ventana.tblpersona.setItem(fila, 2, QTableWidgetItem(objPersona[2]))
            self.ventana.tblpersona.setItem(fila, 3, QTableWidgetItem(objPersona[3]))
            self.ventana.tblpersona.setItem(fila, 4, QTableWidgetItem(objPersona[4]))
            self.ventana.tblpersona.setItem(fila, 5, QTableWidgetItem(objPersona[5]))
            self.ventana.tblpersona.setItem(fila, 6, QTableWidgetItem(objPersona[6]))
            self.ventana.tblpersona.setItem(fila, 7, QTableWidgetItem(objPersona[7]))
            self.ventana.tblpersona.setItem(fila, 8, QTableWidgetItem(objPersona[8]))
            fila =+1

    def listarDocumentos(self):
        self.ventana.cbotipodocumento.addItem("DNI")
        self.ventana.cbotipodocumento.addItem("RUC")