class FacturaDet:
    
    def __init__(self, idFacturaDet, idFactura, idArticulo, cantidad, precio, total_por_linea):
        self.__idFacturaDet = idFacturaDet
        self.__idFactura = idFactura
        self.__idArticulo = idArticulo
        self.__cantidad = cantidad
        self.__precio = precio
        self.__total_por_linea = total_por_linea

    def set_idFacturaDet(self, idFacturaDet):
        self.__idFacturaDet = idFacturaDet    
    def set_idFactura(self, idFactura):
        self.__idFactura = idFactura
    def set_idArticulo(self, idArticulo):
        self.__idArticulo = idArticulo
    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad
    def set_precio(self, precio):
        self.__precio = precio
    def set_total_por_linea(self, total_por_linea):
        self.__total_por_linea = total_por_linea

    def get_idFacturaDet(self, idFacturaDet):
        return self.__idFacturaDet
    def get_idFactura(self, idFactura):
        return self.__idFactura
    def get_idArticulo(self, idArticulo):
        return self.__idArticulo
    def get_cantidad(self, cantidad):
        return self.__cantidad
    def get_precio(self, precio):
        return self.__precio
    def get_total_por_linea(self, total_por_linea):
        return self.__total_por_linea
