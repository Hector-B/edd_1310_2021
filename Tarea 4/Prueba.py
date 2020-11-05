from Archivos import Archivo

datos = Archivo('junio.dat')
datos.calcular_Sueldo('Nombres', 'Sueldo base', 'Año de ingreso', 'Horas extra', 276.5)
datos.empleado_mas_Antiguo('Año de ingreso', 'Nombres', 'Paterno')
datos.empleado_mas_Reciente('Año de ingreso', 'Nombres', 'Paterno')
