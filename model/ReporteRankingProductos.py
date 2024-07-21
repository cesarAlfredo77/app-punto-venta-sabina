from model.Reporte import Reporte

class ReporteRankingProductos(Reporte):

    def __init__(self, idReporte, idEmpleado, titulo, serieReport, nroReport, fechaReport, pieReport, idReporteRankingProd, idFacturaDet, nroFactura, fechaFact, codigoArt, 
                 descripcion, totalcantxproducto, totalxproducto):
        super().__init__(idReporte, idEmpleado, titulo, serieReport, nroReport, fechaReport, pieReport)
        self.__idReporteRankingProd = idReporteRankingProd
        self.__idFacturaDet = idFacturaDet
        self.__nroFactura = nroFactura
        self.__fechaFact = fechaFact
        self.__codigoArt = codigoArt
        self.__descripcion = descripcion
        self.__totalcantxproducto = totalcantxproducto
        self.__totalxproducto = totalxproducto

    def set_idReporteRankingProd(self, idReporteRankingProd):
        self.__idReporteRankingProd = idReporteRankingProd
    def set_idFacturaDet(self, idFacturaDet):
        self.__idFacturaDet = idFacturaDet
    def set_nroFactura(self, nroFactura):
        self.__nroFactura = nroFactura
    def set_fechaFact(self, fechaFact):
        self.__fechaFact = fechaFact
    def set_codigoArt(self, codigoArt):
        self.__codigoArt = codigoArt
    def set_descripcion(self, descripcion):
        self.__descripcion = descripcion
    def set_totalcantxproducto(self, totalcantxproducto):
        self.__totalcantxproducto = totalcantxproducto
    def set_totalxproducto(self, totalxproducto):
        self.__totalxproducto = totalxproducto
    

    def get_idReporteRankingProd(self, idReporteRankingProd):
        return self.__idReporteRankingProd
    def get_idFacturaDet(self, idFacturaDet):
        return self.__idFacturaDet
    def get_nroFactura(self, nroFactura):
        return self.__nroFactura
    def get_fechaFact(self, fechaFact):
        return self.__fechaFact
    def get_codigoArt(self, codigoArt):
        return self.__codigoArt
    def get_descripcion(self, descripcion):
        return self.__descripcion
    def get_totalcantxproducto(self, totalcantxproducto):
        return self.__totalcantxproducto
    def get_totalxproducto(self, totalxproducto):
        return self.__totalxproducto

    def imprimehijoRanking(self):
        return f"Nro. Factura: {self.__nroFactura}, codigoArt: {self.__codigoArt},totalcantxproducto: {self.__totalcantxproducto}, totalxproducto: {self.__totalxproducto}"



    

