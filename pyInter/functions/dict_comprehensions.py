def run():
    # crear un diccionario que las lleves sean del 1 al 100 y los valores sus cubos
    dict_compre = {i : i**3 for i in range(1,101)}
    
    print(dict_compre)

if __name__ == "__main__":
    run()