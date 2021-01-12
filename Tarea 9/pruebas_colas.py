from colas_prioridad import PriorityQueue

barco = PriorityQueue()
barco.enqueue("Maestre", 4)
barco.enqueue("Niños", 2)
barco.enqueue("Mecanico", 4)
barco.enqueue("Hombres", 3)
barco.enqueue("Vigia", 4)
barco.enqueue("capitan", 5)
barco.enqueue("Timonel", 4)
barco.enqueue("Mujeres", 3)
barco.enqueue("3ra edad ", 2)
barco.enqueue("Niñas", 1)

while not barco.is_empty():
    barco.to_string()
    sig = barco.dequeue()
    print(f"Los que evacuaran el barco ahora seran los {sig}")
barco.to_string()
print("Ya no queda nadie por evacuar")
