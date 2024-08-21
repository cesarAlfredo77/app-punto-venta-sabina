class Empleado:

    def __init__(self, idEmpleado, idPersona, area, puesto, correoEmpresa, sueldo):
        self.__idEmpleado = idEmpleado
        self.__idPersona = idPersona
        self.__area = area
        self.__puesto = puesto
        self.__correoEmpresa = correoEmpresa
        self.__sueldo = sueldo

    def set_idEmpleado(self, idEmpleado):
        self.__idEmpleado = idEmpleado
    def set_idPersona(self,idPersona):
        self.__idPersona = idPersona
    def set_area(self, area):
        self.__area = area
    def set_puesto(self, puesto):
        self.__puesto = puesto
    def set_correoEmpresa(self, correoEmpresa):
        self.__correoEmpresa = correoEmpresa
    def set_sueldo(self, sueldo):
        self.__sueldo = sueldo

    def get_idEmpleado(self):
        return self.__idEmpleado
    def get_idPersona(self):
        return self.__idPersona
    def get_area(self):
        return self.__area
    def get_puesto(self):
        return self.__puesto
    def get_correoEmpresa(self):
        return self.__correoEmpresa
    def get_sueldo(self):
        return self.__sueldo
    
 #   def imprimeEmpleado(self):
 #       return f"Desde padre {super().imprimedatosPersona()}, Desde el hijo area: {self.__area}, puesto: {self.__puesto}, sueldo: {self.__sueldo}"


    
#from model.Persona import Persona

#class Empleado(Persona):

#    def __init__(self, idPersona, tipoDoc, numDoc, nombres, apellidos, fechaNac, telefono, 
#                 correo, direccion, idEmpleado, area, puesto, correoEmpresa, sueldo):
#        super().__init__(idPersona, tipoDoc, numDoc, nombres, apellidos, fechaNac, telefono, correo, direccion)
