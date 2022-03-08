""" Un generador es una funcion que guarda un estado. Es sugar sintaxis de un iterador.
    La kwyWorld yield funciona como un return pero guardara el estado de la funcion """

def generator():
    print("Hola 1")
    n=0
    yield n
    
    print("Hola 2")
    n=1
    yield n

    print("Hola 3")
    n=2
    yield n

a = generator()
print(next(a))
print(next(a))
print(next(a))
# print(next(a)) # StopIteration


"""Generator Expresion"""
print()
num = [1,2,3,4,5]

l_compre = [x**2 for x in num]
l_generator = (x**2 for x in num) # Generara iteradores de los elementos (que no se guardan en memoria, se calculan uno a uno)

# while True:
#     try:
#         print(next(l_generator))
#     except StopIteration:
#         break

for n in l_generator:
    print(n)