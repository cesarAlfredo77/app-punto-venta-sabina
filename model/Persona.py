class Persona:

    def __init__(self, idPersona, tipoDoc, numDoc, nombres, apellidos, fechaNac, telefono, correo, direccion):
        self.__idPersona = idPersona
        self.__tipoDoc = tipoDoc
        self.__numDoc = numDoc
        self.__nombres = nombres
        self.__apellidos = apellidos
        self.__fechaNac = fechaNac
        self.__telefono = telefono
        self.__correo = correo
        self.__direccion = direccion

    def set_idPersona(self, idPersona):
        self.__idPersona = idPersona
    def set_tipoDoc(self, tipoDoc):
        self.__tipoDoc = tipoDoc
    def set_numDoc(self, numDoc):
        self.__numDoc = numDoc
    def set_nombres(self, nombres):
        self.__nombres = nombres
    def set_apellidos(self, apellidos):
        self.__apellidos = apellidos
    def set_fechaNac(self, fechaNac):
        self.__fechaNac = fechaNac
    def set_telefono(self, telefono):
        self.__telefono = telefono
    def set_correo(self, correo):
        self.__correo = correo
    def set_direccion(self, direccion):
        self.__direccion = direccion
    
    def get_idPersona(self, idPersona):
        return self.__idPersona
    def get_tipoDoc(self, tipoDoc):
        return self.__tipoDoc
    def get_numDoc(self, numDoc):
        return self.__numDoc
    def get_nombres(self, nombres):
        return self.__nombres
    def get_apellidos(self, apellidos):
        return self.__apellidos
    def get_fechaNac(self, fechaNac):
        return self.__fechaNac
    def get_telefono(self, telefono):
        return self.__telefono
    def get_correo(self, correo):
        return self.__correo
    def get_direccion(self, direccion):
        return self.__direccion

    def imprimePersona(self):
        return "Desde padre"
    def imprimedatosPersona(self):
        return f"Nombres: {self.__nombres}, Apellidos: {self.__apellidos}, Nro. Doc.: {self.__numDoc}"



    

