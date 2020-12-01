from listacircular import CircularList

lc = CircularList()
print(f"¿L esta vacia?: { lc.is_empty() }")
lc.insert(10)
lc.insert(20)
lc.insert(6)
lc.insert(16)
lc.transversal()
print(f"La lista tiene {lc.get_size()} elementos")
lc.insert(8)
lc.transversal()
lc.remove(8)
lc.transversal()
