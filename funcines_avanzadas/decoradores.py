from datetime import datetime

def decorador(func):
    def envoltura():
        print("Esto se añade a mi funcion original")
        func()
    return envoltura

def saludo():
    print("Hola")

# saludo() #Hola

saludo = decorador(saludo)
saludo() #Esto se añade a mi funcion origina, hola

@decorador
def saludo2():
    print("Hola2")

print()
saludo2()

""" Segundo ejemplo """
print()

def mayusculas(func):
    def envoltura(texto):
        return func(texto).upper()
    return envoltura

@mayusculas
def mensaje(nombre):
    return f"{nombre}, recibiste un mensaje"

print(mensaje("Cesar"))


"""Tercer ejemplo"""
print()

def decorator(func):
    def wrapper(a, b):
        print("Comportamiento añadido")
        print(func(a, b))
    return wrapper

@decorator
def suma(a, b):
    return a + b

suma(1,2)

""" Cuarto ejemplo"""
print()

#Funcion que mide el tiempo que tarda en ejecutarse una funcion
def execution_time(func):
    #TODO: *args, **kwargs hacen que la funcion se ejecute con los argumentos necesarios
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        print(final_time - initial_time)
        
    return wrapper

@execution_time
def f_print():
    for _ in range(10000):
        for _ in range(10000):
            pass

@execution_time
def suma(a, b):
    return a + b

@execution_time
def print_nombre(nombre):
    print(nombre)

#f_print()
suma(1,2)
print_nombre("Uriel")


""" Quinto ejemplo con parametros en el decorador """
print()

def with_custom_message(message):
    def with_mesagge(func):
        print(f"{message}: ")
        def wrapper(*args, **kwargs):
            func(*args, **kwargs)
        return wrapper
    return with_mesagge

@with_custom_message("Hola")
def multiply(a, b, c):
    d = a*b*c
    print(f"The result is {d}")

multiply(1,1,2)