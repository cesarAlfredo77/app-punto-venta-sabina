class GrupoCliente:
    
    def __init__(self, idGrupoCli, nombre, beneficio):
        self.__idGrupoCli = idGrupoCli
        self.__nombre = nombre
        self.__beneficio = beneficio


 
    def set_idGrupoCli(self, idGrupoCli):
        self.__idGrupoCli = idGrupoCli
    def set_nombre(self, nombre):
        self.__nombre = nombre
    def set_beneficio(self, beneficio):
        self.__beneficio = beneficio


    def get_idGrupoCli(self, idGrupoCli):
        return self.__idGrupoCli
    def get_nombre(self, nombre):
        return self.__nombre
    def get_beneficio(self, beneficio):
        return self.__beneficio

