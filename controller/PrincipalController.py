from PyQt5 import QtWidgets, uic
from controller.CategoriaController import CategoriaController
from controller.ArticuloController import ArticuloController
from controller.PersonaController import PersonaController
from controller.GrupoClienteController import GrupoClienteController
from controller.EmpleadoController import EmpleadoController

class PrincipalController:

    def __init__(self):
        #app = QtWidgets.QApplication([])
        self.ventana = uic.loadUi("view/frmprincipal.ui")
        self.ventana.show()
        self.ventana.actionCategoria.triggered.connect(self.actionCategoriaClick)
        self.ventana.actionArticulo.triggered.connect(self.actionArticuloClick)
        self.ventana.actionPersona.triggered.connect(self.actionPersonaClick)
        self.ventana.actionGrupo_Cliente.triggered.connect(self.actionGrupoClienteClick)
        self.ventana.actionEmpleado.triggered.connect(self.actionEmpleadoClick)
        self.ventana.actionCerrar_Sesion.triggered.connect(self.cerrarVentana)
        #app.exec()
    
    def actionCategoriaClick(self):
        self.formCategoria = CategoriaController()
        self.formCategoria.ventana.show()

    def actionArticuloClick(self):
        self.formArticulo = ArticuloController()
        self.formArticulo.ventana.show()
    
    def actionPersonaClick(self):
        self.formPersona = PersonaController()
        self.formPersona.ventana.show()

    def actionGrupoClienteClick(self):
        self.formGrupoCli = GrupoClienteController()
        self.formGrupoCli.ventana.show()
    
    def actionEmpleadoClick(self):
        self.formEmpleado = EmpleadoController()
        self.formEmpleado.ventana.show()
    
    def cerrarVentana(self):
        self.ventana.close()
    
