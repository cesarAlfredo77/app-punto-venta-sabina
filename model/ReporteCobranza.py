from model.Reporte import Reporte

class ReporteCobranza(Reporte):

    def __init__(self, idReporte, idEmpleado, titulo, serieReport, nroReport, fechaReport, pieReport, idReporteCobranza, idCobranza, nroFactura, totalCobrado, 
                 totalxCobrar, fechaFact, nroDiasVencidos):
        super().__init__(idReporte, idEmpleado, titulo, serieReport, nroReport, fechaReport, pieReport)
        self.__idReporteCobranza = idReporteCobranza
        self.__idCobranza = idCobranza

        self.__nroFactura = nroFactura
        self.__totalCobrado = totalCobrado
        self.__totalxCobrar = totalxCobrar
        self.__fechaFact = fechaFact
        self.__nroDiasVencidos = nroDiasVencidos

    def set_idReporteCobranza(self, idReporteCobranza):
        self.__idReporteCobranza = idReporteCobranza
    def set_idCobranza(self, idCobranza):
        self.__idCobranza = idCobranza

    def set_nroFactura(self, nroFactura):
        self.__nroFactura = nroFactura
    def set_totalCobrado(self, totalCobrado):
        self.__totalCobrado = totalCobrado
    def set_totalxCobrar(self, totalxCobrar):
        self.__totalxCobrar = totalxCobrar
    def set_fechaFact(self, fechaFact):
        self.__fechaFact = fechaFact
    def set_nroDiasVencidos(self, nroDiasVencidos):
        self.__nroDiasVencidos = nroDiasVencidos
    

    def get_idReporteCobranza(self, idReporteCobranza):
        return self.__idReporteCobranza
    def get_idCobranza(self, idCobranza):
        return self.__idCobranza

    def get_nroFactura(self, nroFactura):
        return self.__nroFactura
    def get_totalCobrado(self, totalCobrado):
        return self.__totalCobrado
    def get_totalxCobrar(self, totalxCobrar):
        return self.__totalxCobrar
    def get_fechaFact(self, fechaFact):
        return self.__fechaFact
    def get_nroDiasVencidos(self, nroDiasVencidos):
        return self.__nroDiasVencidos
    
    def imprimecobranza(self):
        return "Desde el hijo"
    
    def imprimehijo(self):
        return f"{super().imprime()}, Nro. Factura: {self.__nroFactura}, totalCobrado: {self.__totalCobrado}"
    
    



    

