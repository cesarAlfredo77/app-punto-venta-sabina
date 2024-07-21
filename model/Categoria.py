class Categoria:
    
    def __init__(self, idCategoria, nombre, descripcion, estado):
        self.__idCategoria = idCategoria
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__estado = estado

 
    def set_idCategoria(self, idCategoria):
        self.__idCategoria = idCategoria
    def set_nombre(self, nombre):
        self.__nombre = nombre
    def set_descripcion(self, descripcion):
        self.__descripcion = descripcion
    def set_estado(self, estado):
        self.__estado = estado

    def get_idCategoria(self, idCategoria):
        return self.__idCategoria
    def get_nombre(self, nombre):
        return self.__nombre
    def get_descripcion(self, descripcion):
        return self.__descripcion
    def get_estado(self, estado):
        return self.__estado

