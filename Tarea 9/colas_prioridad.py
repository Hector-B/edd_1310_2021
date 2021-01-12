class PriorityQueue:
    def __init__(self):
        self.__data = list()

    def is_empty (self):
        return len(self.__data)==0

    def length(self):
        return len(self.__data)

    def reorder_queue(self, queue):
        return sorted(queue, key=lambda v: v[1])

    def enqueue(self, value: str, priority: int) -> None:
        self.__data.append((value, priority))
        self.__data = self.reorder_queue(self.__data)

    def dequeue(self):
        if not self.is_empty():
            return self.__data.pop(0)
        else:
            return None

    def to_string (self):
        cadena = ""
        for elem in self.__data:
            cadena = cadena + "|" + str(elem)
        cadena = cadena +"|"
        return cadena
