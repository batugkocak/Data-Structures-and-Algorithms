class Deque():
    def __init__(self):
        self.elements = []

    def isEmpty(self):
        return self.elements==[]

    def showAll(self):
        print(self.elements)

    def add(self, element):
        self.elements.append(element)

    def addLeft(self, element):
        self.elements.insert(0, element)

    def remove(self):
        return self.elements.pop()

    def removeLeft(self):
        return self.elements.pop(0)


myDeque = Deque()

myDeque.add(10)
myDeque.add(20)
myDeque.showAll()
myDeque.addLeft(0)
myDeque.showAll()
myDeque.add(50)
myDeque.showAll()

myDeque.remove()
myDeque.removeLeft()

myDeque.showAll()