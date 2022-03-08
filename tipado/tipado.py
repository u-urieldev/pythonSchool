#Funcion de tipado estatico -> tipo de dato que regresa la funcion
def suma(a: int, b: int) -> int:
    return a + b

if __name__ == "__main__":
    #Utilizar mypy <archivo> --check-untyped-defs
    #tipado estatico: variable: tipo=valor
    a: int=5
    b: str="Hola"
    c: bool=True
    
    print(a)
    print(suma(a, 5))

    positives: list[int] = [1,2,3,4,5]
    users: dict[str, int] = {'mexico': 19, 'argentina':21, 'chile':27}
    countries: list[dict[str, str]] = [
	{
		"name" : "Argentina",
		"people" : "45000",
	},
	{
		"name" : "México",
		"people" : "9000000",
	},
	{
		"name" : "Colombia",
		"people" : "99999999999",
	}
]

    print(positives[0])
    print(users['mexico'])
    print(countries[0])

    numbers: tuple[int, float, int]=(1, 2.5, 2) 
