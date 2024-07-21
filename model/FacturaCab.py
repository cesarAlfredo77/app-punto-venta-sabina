class FacturaCab:
    
    def __init__(self, idFactura, idCliente, nroFactura, fechaDoc, moneda, 
                 subTotal, igv, total, comentario, docBaja, idEmpleado, idSalidaInv):
        self.__idFactura = idFactura
        self.__idCliente = idCliente
        self.__nroFactura = nroFactura
        self.__fechaDoc = fechaDoc
        self.__moneda = moneda
        self.__subTotal = subTotal
        self.__igv = igv
        self.__total = total
        self.__comentario = comentario
        self.__docBaja = docBaja
        self.__idEmpleado = idEmpleado
        self.__idSalidaInv = idSalidaInv
    
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
    def set_subTotal(self, subTotal):
        self.__subTotal = subTotal
    def set_igv(self, igv):
        self.__igv = igv
    def set_total(self, total):
        self.__total = total
    def set_comentario(self, comentario):
        self.__comentario = comentario
    def set_docBaja(self, docBaja):
        self.__docBaja = docBaja
    def set_idEmpleado(self, idEmpleado):
        self.__idEmpleado = idEmpleado
    def set_idSalidaInv(self, idSalidaInv):
        self.__idSalidaInv = idSalidaInv

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
    def get_subTotal(self, subTotal):
        return self.__subTotal
    def get_igv(self, igv):
        return self.__igv
    def get_total(self, total):
        return self.__total
    def get_comentario(self, comentario):
        return self.__comentario
    def get_docBaja(self, docBaja):
        return self.__docBaja
    def get_idEmpleado(self, idEmpleado):
        return self.__idEmpleado
    def get_idSalidaInv(self, idSalidaInv):
        return self.__idSalidaInv