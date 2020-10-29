from Arrays import Array

algo = Array(10)
print(algo.get_Item(6363))
algo.set_Item(555,3)
print(algo.get_Item(3))
print( f"El arreglo tiene { algo.get_length() } elementos" )
algo.clear(777 )
print(algo.get_Item(3))
print("----Prueba de iterador----")
for x in range(algo.get_length()):
    print(f"{x} -> {algo.get_Item(x)}")
