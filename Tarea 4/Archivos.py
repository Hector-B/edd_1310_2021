import pandas as np
from datetime import datetime

class Archivo:
    def __init__ (self, nombre):
        try:
            self.__info = np.read_csv(nombre, sep=',')
            print(self.__info)
        except Exception as e:
            print("Archivo no encontrado/incorrecto")

    def calcular_Sueldo(self, colN, colSB, colAI, colHE, horae):
        now = datetime.now()
        for j in range(len(self.__info)):
            prestacion = (now.year-self.__info[' '+colAI][j]) *.03
            sueldo = self.__info[' '+colSB][j] + (horae * self.__info[' '+colHE][j]) + (self.__info[' '+colSB][j]*prestacion)
            print(self.__info[' '+colN][j]+": Sueldo base: " + str(self.__info[' '+colSB][j]) +", Año de ingreso: " + str(self.__info[' '+colAI][j])
             + ", Horas extra: " + str(self.__info[' '+colHE][j]) + ", Prestacion: " + str(prestacion))
            print("Sueldo final: " + str(sueldo))

    def empleado_mas_Reciente(self, colAI, colN, colA):
        menor = max(self.__info[' '+colAI])
        for j in range(len(self.__info)):
            if self.__info[' '+colAI][j] == menor:
                print("Empleado con menor antiguedad: " + self.__info[' '+colN][j] +' '+ self.__info[' '+colA][j])

    def empleado_mas_Antiguo(self, colAI, colN, colA):
        mayor = min(self.__info[' '+colAI])
        for j in range(len(self.__info)):
            if self.__info[' '+colAI][j] == mayor:
                print("Empleado con mayor antiguedad: " + self.__info[' '+colN][j] +' '+ self.__info[' '+colA][j])
