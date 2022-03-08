
# Cuando una funcion generadora ya no tiene mas yields lanza la StopIteration
def fibbonaci_gen(max):
    anterior = 0
    actual = 1
    counter = 0

    while True:
        if counter == 0:
            counter += 1
            yield 0
        elif counter == 1:
            counter += 1
            yield 1
        elif counter < max:
            result = anterior + actual
            anterior, actual = actual, result
            counter += 1
            yield result
        else:
            break

#Funcion mas compacta
def fibonacci_gen_comp(max):
    a, b = 0, 1
    count = 0
    while count < max:
        yield a
        a, b = b, a+b
        count += 1

if __name__ == "__main__":
    serie = fibonacci_gen_comp(7)

    for num in serie:
        print(num)

    # while True:
    #     try:
    #         next(serie)
    #     except StopIteration:
    #         break