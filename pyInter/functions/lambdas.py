def palindrome(string):
    return string == string[::-1]


def run():
    print(palindrome("ana"))

    # Estructura lambdas: LAMBDA parametros: valor retorno (la funcion lambda regresa un valor de tipo funcion)
    palindromel = lambda string: string == string[::-1]
    print(palindromel("ana"))

    square = lambda num: num**2

    print(square(2))    

if __name__ == "__main__":
    run()