class Articulo:
    #Con encapsulamiento

    def __init__(self, idArticulo, idCategoria, codigo, descripcion, und_medida, stock, estado):
        self.__idArticulo = idArticulo
        self.__idCategoria = idCategoria
        self.__codigo = codigo
        self.__descripcion = descripcion
        self.__und_medida = und_medida
    
    def set_idArticulo(self, idArticulo):
        self.__idArticulo = idArticulo
    def set_idCategoria(self, idCategoria):
        self.__idCategoria = idCategoria
    def set_codigo(self, codigo):
        self.__codigo = codigo
    def set_descripcion(self, descripcion):
        self.__descripcion = descripcion
    def set_und_medida(self, und_medida):
        self.__und_medida = und_medida
    def set_stock(self, stock):
        self.__stock = stock
    def set_estado(self, estado):
        self.__estado = estado
    
    def get_idArticulo(self, idArticulo):
        return self.__idArticulo
    def get_idCategoria(self, idCategoria):
        return self.__idCategoria
    def get_codigo(self, codigo):
        return codigo
    def get_descripcion(self, descripcion):
        return descripcion
    def get_und_medida(self, und_medida):
        return und_medida
    def get_stock(self, stock):
        return stock
    def get_estado(self, estado):
        return estado
    
    

