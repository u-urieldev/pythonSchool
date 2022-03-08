# Crear diccionario vacio
my_set = {} # Esto creara un diccionario
print(type(my_set))
my_set = set()
print(type(my_set))

my_list = [1,1,2,3,3,4,4,5,5]
n_set = set(my_list)
print(n_set)

n_set.add(4)
print(n_set)

n_set.add(6)
print(n_set)

#Update necesita un objeto iterable
n_set.update((7,8,9))
print(n_set)

n_set.update({10, 11})
print(n_set)

n_set.discard(1) # n_set.remove(2)
print(n_set)

# Con remove no se pueden borrar elementos inexistentes y lanzara KeyError

n_set.pop() #Borra un elemento aleatorio

n_set.clear()
print(n_set)

""" Operaciones """
print("\n Operaciones")
set1 = {1,2,3,4}
set2 = {4,5,6,7}

#Union
print(set1 | set2)
print(set1.union(set2))

#Interseccion
print(set1 & set2)
print(set1.intersection(set2))

# Diferencia
print(set1 - set2)
print(set1.difference(set2))

# Diferencia simetrica
print(set1 ^ set2)
print(set1.symmetric_difference(set2))