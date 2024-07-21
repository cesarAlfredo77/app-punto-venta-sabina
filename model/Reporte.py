class Reporte:

    def __init__(self, idReporte, idEmpleado, titulo, serieReport, nroReport, fechaReport, pieReport):
        self.__idReporte = idReporte
        self.__idEmpleado = idEmpleado
        self.__titulo = titulo
        self.__serieReport = serieReport
        self.__nroReport = nroReport
        self.__fechaReport = fechaReport
        self.__pieReport = pieReport

    def set_idReporte(self, idReporte):
        self.__idReporte = idReporte
    def set_idEmpleado(self, idEmpleado):
        self.__idEmpleado = idEmpleado
    def set_titulo(self, titulo):
        self.__titulo = titulo
    def set_serieReport(self, serieReport):
        self.__serieReport = serieReport
    def set_nroReport(self, nroReport):
        self.__nroReport = nroReport
    def set_fechaReport(self, fechaReport):
        self.__fechaReport = fechaReport
    def set_pieReport(self, pieReport):
        self.__pieReport = pieReport
    

    def get_idReporte(self, idReporte):
        return self.__idReporte
    def get_idEmpleado(self, idEmpleado):
        return self.__idEmpleado
    def get_titulo(self, titulo):
        return self.__titulo
    def get_serieReport(self, serieReport):
        return self.__serieReport
    def get_nroReport(self, nroReport):
        return self.__nroReport
    def get_fechaReport(self, fechaReport):
        return self.__fechaReport
    def get_pieReport(self, pieReport):
        return self.__pieReport
    
    def imprime(self):
        return "Desde padre"
    



    

