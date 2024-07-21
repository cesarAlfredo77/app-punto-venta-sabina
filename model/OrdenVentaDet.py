class OrdenVentaDet:
    
    def __init__(self, idOrdenVentaDet, idArticulo, idOrdenVenta, cantidad, precio, total_por_linea):
        self.__idOrdenVentaDet = idOrdenVentaDet
        self.__idArticulo = idArticulo
        self.__idOrdenVenta = idOrdenVenta
        self.__cantidad = cantidad
        self.__precio = precio
        self.__total_por_linea = total_por_linea
    
    def set_idOrdenVentaDet(self, idOrdenVentaDet):
        self.__idOrdenVentaDet = idOrdenVentaDet
    def set_idArticulo(self, idArticulo):
        self.__idArticulo = idArticulo
    def set_idOrdenVenta(self, idOrdenVenta):
        self.__idOrdenVenta = idOrdenVenta
    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad
    def set_precio(self, precio):
        self.__precio = precio
    def set_total_por_linea(self, total_por_linea):
        self.__total_por_linea = total_por_linea

    def get_idOrdenVentaDet(self, idOrdenVentaDet):
        return self.__idOrdenVentaDet
    def get_idArticulo(self, idArticulo):
        return self.__idArticulo
    def get_idOrdenVenta(self, idOrdenVenta):
        return self.__idOrdenVenta
    def get_cantidad(self, cantidad):
        return self.__cantidad
    def get_precio(self, precio):
        return self.__precio
    def get_total_por_linea(self, total_por_linea):
        return self.__total_por_linea
