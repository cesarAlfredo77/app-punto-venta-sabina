from PyQt5 import QtWidgets, uic
from controller.PrincipalController import PrincipalController

class LoginController:

    def __init__(self):
        app = QtWidgets.QApplication([])
        self.ventana = uic.loadUi("view/frmlogin.ui")
        self.ventana.show()
        self.ventana.btniniciarsesion.clicked.connect(self.iniciarSesionClick)
        self.ventana.btnsalir.clicked.connect(self.cerrarVentana)
        app.exec()
    
    def iniciarSesionClick(self):
        self.formPrincipal = PrincipalController()
        self.formPrincipal.ventana.show()
    
    def cerrarVentana(self):
        self.ventana.close()
    