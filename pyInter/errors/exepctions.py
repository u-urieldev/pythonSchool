def palindorme(string):
    try:
        if len(string) == 0:
            raise ValueError("No se pueden ingresar cadenas vacías")
        return string == string[::-1]
    except ValueError as ve:
        print(ve)
        return False

def palindrome_assert(string):
    #Estructuras de assert: afirmacion, mensaje si no se cumple
    assert len(string) > 0, "No se pueden ingresar cadenas vacías"
    return string == string[::-1]

def run():
    try:
        palindorme("") #Esto arrojara una TypeError exepction
    except TypeError:
        print("Poner solo strings")

    palindrome_assert("")
    

if __name__ == "__main__":
    run()