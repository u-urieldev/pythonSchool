def run():
    # Crea una lista con el cuadrado de los 100 primeros 
    # numeros enteros que no sean divisibles entre 3
    """
    square = []

    for i in range (1, 101):
        if i%3 != 0:
            square.append(i**2)

    for elem in square:
        print(elem)
    """

    # Usando list_comprehensions
    # Estructura: [element FOR element IN iterable IF condition]

    square = [i**2 for i in range(1, 101) if i%3 != 0]

    for elem in square:
        print(elem)

    """
    # Todos los multiplos de 4 que tambien sean multiplos de 6 y 9 y sean menores a 5 digitos.
    lc = [i for i in range(1, 1000000) if (i%4 == 0 and i%6 == 0 and i%9 == 0)]

    for elem in lc:
        print(elem)
    """

if __name__ == "__main__":
    run()