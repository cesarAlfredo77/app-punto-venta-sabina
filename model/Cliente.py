from model.Persona import Persona

class Cliente(Persona):

    def __init__(self, idPersona, tipoDoc, numDoc, nombres, apellidos, fechaNac, telefono, correo, direccion, idCliente, idGrupoCli, estContribuyente, condContribuyente, 
                 lineaCredito, condPago):
        super().__init__(idPersona, tipoDoc, numDoc, nombres, apellidos, fechaNac, telefono, correo, direccion)
        self.__idCliente = idCliente
        self.__idGrupoCli = idGrupoCli
        self.__estContribuyente = estContribuyente
        self.__condContribuyente = condContribuyente
        self.__lineaCredito = lineaCredito
        self.__condPago = condPago


    def set_idCliente(self, idCliente):
        self.__idCliente = idCliente
    def set_idGrupoCli(self, idGrupoCli):
        self.__idGrupoCli = idGrupoCli
    def set_estContribuyente(self, estContribuyente):
        self.__estContribuyente = estContribuyente
    def set_condContribuyente(self, condContribuyente):
        self.__condContribuyente = condContribuyente
    def set_lineaCredito(self, lineaCredito):
        self.__lineaCredito = lineaCredito
    def set_condPago(self, condPago):
        self.__condPago = condPago

    
    def get_idCliente(self, idCliente):
        return self.__idCliente
    def get_idGrupoCli(self, idGrupoCli):
        return self.__idGrupoCli
    def get_estContribuyente(self, estContribuyente):
        return self.__estContribuyente
    def get_condContribuyente(self, condContribuyente):
        return self.__condContribuyente
    def get_lineaCredito(self, lineaCredito):
        return self.__lineaCredito
    def get_condPago(self, condPago):
        return self.__condPago
    
    def imprimeCliente(self):
        return f"Desde cliente, idcliente: {self.__idCliente}, Desde padre {super().imprimedatosPersona()}"

    



    

