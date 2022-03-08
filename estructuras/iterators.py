
def for_loop_explication():
    # Creando un iterador
    my_list = [1,2,3,4,5]
    my_iter = iter(my_list)

    # Iterando un iterador (estructura por dentro del ciclo for)
    while True:
        try:
            elem = next(my_iter)
            print(elem)
        except StopIteration:
            break

#for_loop_explication()

class EvenNumbers:
  """Clase que implementa un iterador de todos los números pares,
  o los números pares hasta un máximo
  """

  #* Constructor de la clase
  def __init__(self, max = None): 
    self.max = max
    self.num = 0 

  # Método para tener elementos o atributos que voy a necesitar para que el iterador funcione
  def __iter__(self):
    self.num = 0 #Primer número par
    #* Convertir un iterable en un iterador
    return self

  # Método para tener la función "next" de Python
  def __next__(self):
    if not self.max or self.num <= self.max:
      result = self.num
      self.num += 2
      return result
    else:
      raise StopIteration


ten = EvenNumbers(10)
while True:
    try:
        elem = next(ten)
        print(elem)
    except StopIteration:
        break