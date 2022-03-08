def func():
    a = 1

    def nested():
        print(a)

    return nested

# my_func contendra nested()
my_func = func() 
# El valor de a es recordado aunque este fuera del scope
my_func()
#Incluso si se borra la funcion seguira guardando el valor de a
del(func)
my_func()


def make_multiplication(x):

    def multiplier(n):
        return x * n
    
    return multiplier

times10 = make_multiplication(10)
times4 = make_multiplication(4)

# times10 y times4 recordaran que x es el parametro pasado anteriormente
# y solo esperaran el argumento de multiplier
print(times10(3))
print(times4(5))
print(times10(times4(2)))


def string_to_multiply(string):
    assert type(string) == str, "Solo puedes utilizar cadenas"
    def times(n):
        print(string * n)

    return times

w_hola = string_to_multiply("Hola")
w_hola(3)


def make_division_by(n):
    assert n != 0, "No puedes dividir entre 0"
    def division(x):
        return x/n
    
    return division

division_by_3 = make_division_by(3)
print(division_by_3(18))