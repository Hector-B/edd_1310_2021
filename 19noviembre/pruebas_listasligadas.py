from listas import LinkedList


l= LinkedList()
print(f"L esta vacia ?{l.is_empty() }")
l.append(10)
l.append(5)
l.append(6)
l.append(20)
print(f"L esta vacia ?{l.is_empty() }")
l.trasversal()
l.remove(10)
l.trasversal()
l.transversal()
l.preppend(80)
l.transversal()
x=l.tail()
print(x.data)
print(l.get())
