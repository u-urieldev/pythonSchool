from Node import Node

class LinkedList():
    def __init__(self, *args) -> None:
        self.head = None
        self.size = 0

        try: 
            if isinstance(args[0], list):
                self.__makefromlist(args[0])
            else:
                self.head = self.append(args[0])
                print("Head")
        except IndexError:
            print("Vacia")
           
    def __makefromlist(self, ls):
        for elem in ls:
            self.append(elem)
                


    def append(self, data):
        node = Node(data)

        if self.head == None:
            self.head = node 
        else:
            current = self.head

            while current.next != None:
                current = current.next

            current.next = node

        self.size += 1
    
    def size(self):
        return self.size

    def iter(self):
        current = self.head

        while current:
            val = current.data
            current = current.next
            yield val

    def delete(self):
        pass

    def search(self):
        pass

    def clear(self):
        pass

    