from colas import Queue,BoundedPriorityQueue
q1= Queue()
q1.enqueue(3)
q1.enqueue(33)
q1.enqueue(23)
print(q1.to_string())


print("Prueba 2 de Queue")
c1={ "id":1 , "nombre":"Mario" , "balance": 20.5 }
c2={ "id":2 , "nombre":"Diana" , "balance": 3456.5 }
c3={ "id":3 , "nombre":"Bartolo" , "balance": 1000000.0 }

atencion = Queue()
atencion.enqueue(c1)
atencion.enqueue(c2)
atencion.enqueue(c3)
print(atencion.to_string())
siguiente = atencion.dequeue()
print(f"Bienvenido sr. {siguiente['nombre'] }, en que podemos servirle el dia de hoy")
print(atencion.to_string())

print("Pruebas de las colas con prioridad acotada")

maestres = {"prioridad":4 , "descripcion":"Maestre" , "personas":["juan p ", "diego h"]}
niños = {"prioridad":2 , "descripcion":"Niños" , "personas":["Santi H ", "Angel h"]}
mecanicos = {"prioridad":4 , "descripcion":"Mecánicos" , "personas":["Diana T ", "Maria 2"]}
mujeres = {"prioridad":3, "descripcion":"mujeres", "Personas":["Andrea T","Sofia H"]}
ancianos = {"prioridad":2, "descripcion":"ancianos", "Personas":["Juan O","Arturo F "]}
niñas = {"prioridad":1, "descripcion":"niñas", "Personas":["Fernanda M ","Miranda A"]}
hombre = {"prioridad":3, "descripcion":"hombre", "Personas":["Ricardo B","Andres D"]}
vigia = {"prioridad":4, "descripcion":"vigia", "Personas":["Johny C","Julian M"]}
capitan = {"prioridad":5, "descripcion":"capitan", "Personas":["Sparrow T","Tom H"]}
timonel = {"prioridad":4, "descripcion":"timonel", "Personas":["Karen P","Cassandra E"]}


cpa = BoundedPriorityQueue( 7 )
cpa.enqueue(maestres['prioridad'], maestres)
cpa.enqueue(niños['prioridad'], niños)
cpa.enqueue(mecanicos['prioridad'], mecanicos)
cpa.enqueue(mujeres['prioridad'], mujeres)
cpa.enqueue(ancianos['prioridad'], ancianos)
cpa.enqueue(niñas['prioridad'], niñas)
cpa.enqueue(hombre['prioridad'], hombre)
cpa.enqueue(vigia['prioridad'], vigia)
cpa.enqueue(capitan['prioridad'], capitan)
cpa.enqueue(timonel['prioridad'], timonel)

while not cpa.is_empty():
    cpa.to_string()
    sig = cpa.dequeue()
    print(f"Los que evacuaran el barco ahora seran los {sig}")
cpa.to_string()
print("Todos han sido evacuados")
