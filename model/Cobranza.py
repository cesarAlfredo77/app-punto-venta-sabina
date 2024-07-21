class Cobranza:

    def __init__(self, idCobranza, idFactura, idCliente, nroFactura, fechaDoc, moneda, 
                 total, comentario, estadoDoc, idEmpleado):
        self.__idCobranza = idCobranza
        self.__idFactura = idFactura
        self.__idCliente = idCliente
        self.__nroFactura = nroFactura
        self.__fechaDoc = fechaDoc
        self.__moneda = moneda
        self.__total = total
        self.__comentario = comentario
        self.__estadoDoc = estadoDoc
        self.__idEmpleado = idEmpleado

    def set_idCobranza(self, idCobranza):
        self.__idCobranza = idCobranza
    def set_idFactura(self, idFactura):
        self.__idFactura = idFactura
    def set_idCliente(self, idCliente):
        self.__idCliente = idCliente
    def set_nroFactura(self, nroFactura):
        self.__nroFactura = nroFactura
    def set_fechaDoc(self, fechaDoc):
        self.__fechaDoc = fechaDoc
    def set_moneda(self, moneda):
        self.__moneda = moneda
    def set_total(self, total):
        self.__total = total
    def set_comentario(self, comentario):
        self.__comentario = comentario
    def set_estadoDoc(self, estadoDoc):
        self.__estadoDoc = estadoDoc
    def set_idEmpleado(self, idEmpleado):
        self.__idEmpleado = idEmpleado
    
    def get_idCobranza(self, idCobranza):
        return self.__idCobranza
    def get_idFactura(self, idFactura):
        return self.__idFactura
    def get_idCliente(self, idCliente):
        return self.__idCliente
    def get_nroFactura(self, nroFactura):
        return self.__nroFactura
    def get_fechaDoc(self, fechaDoc):
        return self.__fechaDoc
    def get_moneda(self, moneda):
        return self.__moneda
    def get_total(self, total):
        return self.__total
    def get_comentario(self, comentario):
        return self.__comentario
    def get_estadoDoc(self, estadoDoc):
        return self.__estadoDoc
    def get_idEmpleado(self, idEmpleado):
        return self.__idEmpleado



    

