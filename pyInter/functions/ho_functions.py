#from functools import reduce
import functools # no funcionaba cuando solo se importaba la funcion 

def is_odd(x):
    return x%2 != 0

def make_square(x):
    return x**2

def reduce():
    super_list = [2,2,2,2,2]
    print("------Reduce-------")

    all_multiplied = functools.reduce(lambda a, b: a*b, super_list)
    print(all_multiplied)
    

def map_example():
    super_list = [1,2,3,4,5]
    print("------Map-------")

    # Crear una lista con los cuadrados de la super lista
    # Utilizando comprehensions
    square_list_compre = [i**2 for i in super_list]
    print(square_list_compre)


    # Utilizando la ho MAP
    # Estructura map(funcion, iterable)

    # Utilizando funcion definida
    square_list_def = list(map(make_square, super_list))
    print(square_list_def)

    # Utilizado funcion anonima
    square_list_lambda = list(map(lambda x: x**2, super_list))
    print(square_list_lambda)


def filter_example():
    super_list = [1,4,5,6,9,13,19,21]
    print("------Filter-------")
    
    #crear una lista apartir de la super lista solo con los numeros impares
    odd_list = [i for i in super_list if i%2 != 0]
    print(odd_list)


    # Utilizando la funcion de orden superior filter
    # filter(bool funcion, iterable)
    
    # Utilizando una funcion definida
    odd_list_filter = list(filter(is_odd, super_list))
    print(odd_list_filter)

    # Utilizando funcion anonima
    odd_list_filter_lambda = list(filter(lambda x: x%2 != 0, super_list))
    print(odd_list_filter_lambda)

    print()

def run():
    #filter_example()
    #map_example()
    reduce()

if __name__ =="__main__":
    run()