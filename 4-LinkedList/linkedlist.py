# Singly Linked List


class Node():
    def __init__(self, value):
        self.value = value
        self.nextNode = None


firstNode = Node(10)
secondNode = Node(20)
thirdNode = Node(30)

firstNode.nextNode = secondNode
secondNode.nextNode = thirdNode

print(firstNode.nextNode.nextNode.value)


class DoublyNode():
    def __init__(self, value):
        self.value = value
        self.nextNode = None
        self.previousNode = None


x = DoublyNode(10)
y = DoublyNode(20)
z = DoublyNode(30)

x.nextNode = y

y.previousNode = x
y.nextNode = z

z.previousNode = y

print(x.nextNode.nextNode.value)
print(z.previousNode.value)  # y

#  Function     | LinkedList | List
#  --------       ----------   ----
#  Append       |   O(1)     O(1)  / -
#  Pop          |   O(n)     O(1) / List
# Prepend       |   O(1)     O(n) / LinkedList
# Pop First     |   O(1)     O(n) / LinkedList
# Access(Index) |   O(n)     O(1) / List
# Access(Value) |   O(n)     O(n) / -
#  Remove       |   O(n)     O(n) / -
# Insert        |   O(n)     O(n) / -


