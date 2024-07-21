
from model.ReporteCobranza import ReporteCobranza
from model.ReporteRankingProductos import ReporteRankingProductos
from model.Cliente import Cliente
from model.Empleado import Empleado

objreporte = ReporteCobranza(1, 5, "Reporte Cobranza 01", "COB2024", 1, "21/07/2024", "PIE", 1, 10, "F001-1234", 200, 
                 50, "01/07/2024", 20)

objreporteproducto = ReporteRankingProductos(1, 2, "Reporte de Ranking producto", "PROD2024", 1, "21/07/2024", "PIE", 1, 3, "F002-3240", "02/07/2024", "LECH0001", 
                 "LECHE GLORIA 500ML", 10, 50)

print(objreporte.imprimecobranza())
print(objreporte.imprime())
print(objreporte.imprimehijo())

print(objreporteproducto.imprimehijoRanking())

objcliente = Cliente(1, "DNI", "42024033", "Luis Miguel", "Minaya Flores", "10/03/1990", "942420475", "luism@gmail.com", "Av. los heroes, San Juan", 10, 2, "ACTIVO", "HABIDO", 
                 1000, "CREDITO A 30 DIAS")

print(objcliente.imprimeCliente())

objempleado = Empleado(2, "DNI", "734230222", "Anderson", "Pineda Saavedra", "14/07/1995", "988230398", 
                 "", "Av. Lirios 1221", 2, "Ventas", "Vendedor", "ventas1@sabina.com", 1700)

print(objempleado.imprimeEmpleado())


