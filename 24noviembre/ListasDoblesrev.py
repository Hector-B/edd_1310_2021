class NodoDoble:
    def __init__( self , value ,  anterior = None , siguiente = None):
        self.data = value
        self.next = siguiente
        self.prev = anterior

class DoubleLinkedList:

    def __init__ ( self ):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def is_empty(self):
        return self.__size ==0

    def get_size(self):
        return self.__size

    def append(self, value):
        if self.is_empty():
            nuevo = NodoDoble(value)
            self.__head = nuevo
            self.__tail = nuevo
        else:
            nuevo = NodoDoble(value, self.__tail, None)
            self.__tail.next = nuevo
            self.__tail = nuevo
        self.__size +=1

    def transversal(self):
        curr_node = self.__head
        while curr_node != None:
            print(f"<--- {curr_node.data} -->", end="")
            curr_node = curr_node.mext
        print("")

    def reverse_transversal(self):
        curr_node = self.__tail
        while curr_node != None:
            print(f"<--- {curr_node.data} -->", end="")
            curr_node = curr_node.prev
        print("")

    def remove_from_head(self, value):
        if self.__head.data == value:
            self.__head = self.__head.next
            self.__head.prev = None
        elif self.__tail.data == value:
            self.__tail.prev.next = None
            self.__tail = self.__tail.prev
        else:
            curr_node = self.__head
            while curr_node.data != value and curr_node != None:
                curr_node = curr_node.next
                if curr_node.data == value:
                    curr_node.prev.next = curr_node.next
                    curr_node.next.prev = curr_node.prev
                else:
                    print("El dato no se encuentra en la lista")
                curr_node.next = None
                curr_node.prev = None
        self.__size -= 1
            
