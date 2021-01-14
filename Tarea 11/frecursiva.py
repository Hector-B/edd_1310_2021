def sucesion(x):
    if x >= 0:
        print(x)
        sucesion(x-1)
    else:
        print("Listo")

def main():
    sucesion(5)

main()
class Stack:
    def __init__(self):
        self.__data=list()

    def is_empty(self):
        return len(self.__data)==0

    def length(self):
        return len(self.__data)

    def pop(self):
        if self.is_empty():
            print("Fila vacia")
        else:
            return self.__data.pop()
    def push(self,value):
        self.__data.append(value)

    def peek(self):
        return self.__data[len(self.__data)-1]

    def to_string(self):
        print("-----")
        for item in self.__data[::-1]:
            print(f"| {item} |")
            print("-----")

def eliminar(pila, size, c) :
    if (pila.is_empty() or c == size) :
        return
    x = pila.peek()
    pila.pop()
    eliminar(pila, size, c+1)
    middle=(size/2)
    if middle == int(middle):
        if (c != middle and c != (middle-1)):
            pila.push(x)
    else:
        if ( c != int(size/2)) :
            pila.push(x)

def main2():
    st = Stack()
    st.push('H')
    st.push('E')
    st.push('C')
    st.push('T')
    st.push('O')
    st.push('R')

    print("---Pila---")
    st.to_string()
    print("-----")
    eliminar(st, st.length(), 0)
    st.to_string()

main2()
