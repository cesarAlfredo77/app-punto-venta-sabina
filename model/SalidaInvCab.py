class SalidaInvCab:

    def __init__(self, idSalidaInv, idCliente, idOrdenVenta, idEmpleado, nroSalidaInv, fechaDoc, moneda, 
                 subTotal, igv, total, comentario):
        self.__idSalidaInv = idSalidaInv
        self.__idCliente = idCliente
        self.__idOrdenVenta = idOrdenVenta
        self.__idEmpleado = idEmpleado
        self.__nroSalidaInv = nroSalidaInv
        self.__fechaDoc = fechaDoc
        self.__moneda = moneda
        self.__subTotal = subTotal
        self.__igv = igv
        self.__total = total
        self.__comentario = comentario

    def set_idSalidaInv(self, idSalidaInv):
        self.__idSalidaInv = idSalidaInv
    def set_idCliente(self, idCliente):
        self.__idCliente = idCliente
    def set_idOrdenVenta(self, idOrdenVenta):
        self.__idOrdenVenta = idOrdenVenta
    def set_idEmpleado(self, idEmpleado):
        self.__idEmpleado = idEmpleado
    def set_nroSalidaInv(self, nroSalidaInv):
        self.__nroSalidaInv = nroSalidaInv
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
    
    def get_idSalidaInv(self, idSalidaInv):
        return self.__idSalidaInv
    def get_idCliente(self, idCliente):
        return self.__idCliente
    def get_idOrdenVenta(self, idOrdenVenta):
        return self.__idOrdenVenta
    def get_idEmpleado(self, idEmpleado):
        return self.__idEmpleado
    def get_nroSalidaInv(self, nroSalidaInv):
        return self.__nroSalidaInv
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



    

