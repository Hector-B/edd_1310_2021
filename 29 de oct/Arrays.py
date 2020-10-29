class Array:
    def __init__(self, tam):
        self.__info = [0 for x in range(tam)]

    def set_Item(self, dato, posicion):
        try:
            self.__info[posicion] = dato
        except Exception as e:
            print("Dato incorrecto")
        return dato

    def get_Item(self, posicion):
        dato = 0
        try:
            dato = self.__info[posicion]
        except Exception as e:
            print("Dato incorrecto")
        return dato

    def clear(self, dato):
        self.__info = [dato for x in range(len(self.__info))]

    def get_lenght(self):
        return len(self.__info)

    def _iter_ (self):
        return _IteradorArreglo(self.__info)

class _IteradorArreglo:
    def __init__( self , arr ):
        self.__arr = arr
        self.__indice = 0

    def iter (self):
        return self

    def __next__(self):
        if self.__indice < len(self.__arr):
            dato = self.__arr[self.__indice]
            self.__indice += 1
            return dato
        else:
            raise StopIteration
