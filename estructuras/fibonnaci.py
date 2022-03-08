class Fibonnaci:
    # Se pide la cantidad de numeros maximos
    def __init__(self, max = None):
        assert type(max) == int, "Debe ser un entero"
        self.max = max

    # El metodo iter contiene los elementos para que el iterador funcione
    def __iter__(self):
        self.anterior = 0
        self.actual = 1
        self.counter = 0
        return self
    
    # El metodo next permite usar next()
    def __next__(self):
        if self.counter == 0:
            self.counter += 1
            return 0
        elif self.counter == 1:
            self.counter += 1
            return 1
        elif self.counter < self.max:
            result = self.anterior + self.actual
            self.anterior, self.actual = self.actual, result
            self.counter += 1
            return result
        else:
            raise StopIteration


if __name__ == "__main__":
    serie = Fibonnaci(7)

    # Con __next__ podremos utilizar la iteracion sobre lista por que ya vimos que se ocupa un ciclo whilw
    for num in serie:
        print(num)

    # while True:
    #     try:
    #         elem = next(serie)
    #         print(elem)
    #     except StopIteration:
    #         break
