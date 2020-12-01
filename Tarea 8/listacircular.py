class Nodo:
    def __init__( self , value , siguiente= None):
        self.data = value
        self.next = siguiente

class CircularList:
    def __init__( self ):
        self.__ref = None
        self.__menor = None
        self.__size= 0

    def is_empty (self):
        return self.__size == 0

    def get_size(self):
        return self.__size

    def insert (self, value ):
        if self.is_empty() :
            self.__menor = self.__ref= Nodo(value)
            self.__ref.next= self.__menor

            self.__size +=1

        elif self.search(value) == True :
              print("El dato ya existe")

        elif value > self.__ref.data:
            nuevo = self.__ref
            self.__ref = nuevo.next= Nodo(value, self.__menor)
            self.__size +=1
        elif value < self.__ref.data and value < self.__menor.data:
             nuevo =  Nodo(value)
             nuevo.next = self.__menor
             self.__menor = nuevo
             self.__ref.next = nuevo
             self.__size +=1

        elif value < self.__ref.data and  value > self.__menor.data:
            nuevo = Nodo(value)
            curr_node= self.__menor
            while nuevo.data > curr_node.next.data:
                curr_node = curr_node.next
            nuevo.next= curr_node.next
            curr_node.next= nuevo
            self.__size +=1




    def search (self, value ):
         nuevo = Nodo(value)
         curr_node= self.__ref
         while nuevo.data != curr_node.next.data and curr_node.next != self.__ref:
                curr_node = curr_node.next
         if nuevo.data == curr_node.next.data :
             return True
         else:

             return False

    def remove( self , value ):
        nuevo = Nodo(value)
        curr_node= self.__ref
        if self.search(value) == False :
              print("No existe el dato que quieres eliminar")
        else:
            while nuevo.data != curr_node.next.data and curr_node.next != self.__ref:
                  curr_node = curr_node.next
            if curr_node.next.data == self.__ref.data:
                curr_node.next =  self.__ref.next
                self.__ref = curr_node
                self.__size -=1

            elif curr_node.next.data == self.__menor.data:
                self.__menor = self.__menor.next
                self.__ref.next = self.__menor
                self.__size -=1

            elif curr_node.next.data != self.__ref.data and curr_node.next.data != self.__menor.data:

                anterior = None

                while curr_node.data != value and curr_node.next != self.__ref:
                      anterior = curr_node
                      curr_node= curr_node.next
                if curr_node.data == value:
                    anterior.next= curr_node.next
                    self.__size -=1














    def transversal (self):
        curr_node = self.__ref
        while curr_node.next != self.__ref :
            print(f"{ curr_node.next.data } --> " , end="")
            curr_node= curr_node.next
        print(self.__ref.data)
        print("")
