class NodoDoble:
    def __init__( self , value , siguiente = None , anterior = None ):
        self.data = value
        self.next = siguiente
        self.prev = anterior

class DoubleLinkedList:

    def __init__ ( self ):
        self.__head = NodoDoble (None , None , None)
        self.__tail = NodoDoble(None , None , None)
        self.__head.next = self.__tail
        self.__tail.prev = self.__head
        self.__size = 0
        print( f" head :{self.__head} ")
        print( f" tail :{self.__tail} ")

    def is_empty(self):
        return self.__head == self.__tail.prev

    def append(self, value):
        nuevo = NodoDoble(value)
        if self.__head == self.__tail:
            self.__head = self.__tail = nuevo
        else:
            curr_node = self.__head
            while curr_node.siguiente != None:
                curr_node = curr_node.siguiente
            curr_node.siguiente = nuevo
            curr_node = self.__tail
            self.__tail = curr_node.siguiente = nuevo
            self.__tail.prev = curr_node
        self.__size += 1

    def transversal(self):
        curr_node = self.__head
        while curr_node != None:
            print(f"{curr_node.data} -->", end="")
            curr_node = curr_node.siguiente
        print("")

    def reverse_transversal(self):
        curr_node = self.__tail
        while curr_node.prev != None:
            print(f"{curr_node.data} -->", end="")
            curr_node = curr_node.prev
        print("")

    def get_Size(self):
        return self.__size

    def find_from_head(self, value):
        curr_node = self.__head
        contador = 0
        bandera = False
        while curr_node != None:
            if curr_node.data == value:
                bandera = True
                print(f"El valor {value} esta en la posicion: {contador}")
            curr_node = curr_node.siguiente
            contador = contador +1
        if bandera == False:
            print("El valor no se encuentra en la lista")

    def find_from_tail(self, value):
        curr_node = self.__tail
        contador = 1
        bandera = False
        while curr_node != None:
            if curr_node.data == value:
                bandera = True
                print(f"El valor {value} esta en la posicion: {contador}")
            curr_node = curr_node.prev
            contador = contador+1
        if bandera == False:
            print("El valor no se encuentra en la lista")

    def remove_from_head(self, value):
        curr_node = self.__head
        if self.__head.data == value:
            self.__head = self.__head.siguiente
            self.remove_from_tail(value)
        else:
            anterior = None
            while curr_node.data != value and curr_node.siguiente != None:
                anterior = curr_node
                curr_node= curr_node.siguiente
            if curr_node.data == value:
                anterior.siguiente = curr_node.siguiente
                self.remove_from_tail(value)
            else:
                print("El dato no existe en la lista")

    def  remove_from_tail(self, value):
        curr_node = self.__tail
        if self.__tail.data == value:
            self.__tail = self.__tail.prev
            self.remove_from_head(value)
        else:
            siguiente = None
            while curr_node.data != value and curr_node.prev != None:
                siguiente = curr_node
                curr_node= curr_node.prev
            if curr_node.data == value:
                siguiente.prev = curr_node.prev
                self.remove_from_head(value)
            else:
                print("El dato no existe en la lista")
