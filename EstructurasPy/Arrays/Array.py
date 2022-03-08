class Array:
    def __init__(self, capacity, fill_value=None) -> None:
        self.items = list([fill_value for _ in range(capacity)])
        
    def printArr(self):
        for elem in self.items:
            print(elem)

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

    def __iter__(self):
        return iter(self.items)

    def comprobar(self, elem):
        return True if elem in self.items else False

    def sumar(self):
        total = 0
        for elem in self.items:
            total += elem
        return total
