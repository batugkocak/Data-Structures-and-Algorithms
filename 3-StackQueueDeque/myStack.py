# Stack()
# push()
# pop()
# showLast()
# size()
# isEmpty()

class Stack():
    def __init__(self):
        self.elements = []

    def isEmpty(self):
        return self.elements == []

    def push (self, element):
        self.elements.append(element)

    def pop(self):
        return self.elements.pop()

    def showLast(self):
        return self.elements[-1]  # self.elements[len(self.elements) -1]

    def size(self):
        return len(self.elements)

myStack = Stack()

print(myStack.isEmpty())

myStack.push(10)
myStack.push(20)
myStack.push(40)
print(myStack)
