from Array2D import Array2D
from stack import Stack
class LaberintoADT:
    """
    0 pasillo, 1 pared, S salida , y E entrada
    pasillo es una tupla ((2,1),(2,2),(2,3), (2,4), (3,2),(4,2))
    entrada es una tupla ( 5,2)
    salida es una tupla ( 2,5)
    """
    def __init__(self , rens , cols , pasillos , entrada , salida ):
        self.__laberinto = Array2D( rens , cols , '1' )
        for pasilo in pasillos:
            self.__laberinto.set_item( pasilo[0], pasilo[1] , '0')
        self.set_entrada(entrada[0],entrada[1])
        self.set_salida(salida[0],salida[1])
        self.__camino = Stack()
        self.__previa = None


    def to_string(self):
        self.__laberinto.to_string()

    """
establece la entreda poniendo una "E" en la matriz
verificar limites
    """
    def set_entrada(self, ren, col ):
        #verificar qye la entrada se encuentre en el permietro .
        self.__laberinto.set_item( ren , col ,'E')

    def set_salida(self, ren , col ):
        self.__laberinto.set_item( ren , col ,'S')
        #Hacer las validaciones

    def es_salida(self , ren , col ):
        return self.__laberinto.get_item(ren,col) == 'S'

    def buscar_entrada(self):
        encontrado= False
        for renglon in range(self.__laberinto.get_num_rows() ):
            for columna in range(self.__laberinto.get_num_cols() ):
                if self.__laberinto.get_item(renglon,columna) == 'E':
                    self.__camino.push( tuple(renglon, columna) )
                    encontrado=True
        return encontrado
                
    def set_previa(self, pos_previa ):
        self.__previa = pos_previa

    def get_previa(self):
        return self.__previa

    def resolver_laberinto(self ):
        #Aplicar reglas
