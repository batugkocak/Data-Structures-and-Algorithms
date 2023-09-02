# BFS : Breadth First Search 

# DFS : Depth First Search 


class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        newNode = Node(value)

        if self.root is None:
            self.root = newNode
            return True
        tempNode = self.root
        while True:
            if newNode.val == tempNode.val:
                return False
            if newNode.val < tempNode.val:  # Left
                if tempNode.left is None:
                    tempNode.left = newNode
                    return True
                else:
                    tempNode = tempNode.left

            if newNode.val > tempNode.val:  # Right
                if tempNode.right is None:
                    tempNode.right = newNode
                    return True
                else:
                    tempNode = tempNode.right

    # -- Insert End --


    def contains(self, val):
        tempNode = self.root
        while tempNode:
            if val < tempNode.val:
                tempNode = tempNode.left
            elif val > tempNode.val:
                tempNode = tempNode.right
            else:
                return True
        return False

    # -- Contains End --


    def minOfNode(self, currentNode):
        while currentNode.left:
            currentNode = currentNode.left
        return currentNode
    def maxOfNode(self, currentNode):
        while currentNode.right:
            currentNode = currentNode.right
        return currentNode

    # -- Max - Min End --


    def BFS(self):
        currentNode = self.root
        myQueue = []
        values = []
        myQueue.append(currentNode)

        while len(myQueue) > 0:
            currentNode = myQueue.pop(0)
            values.append(currentNode.val)
            if currentNode.left is not None:
                myQueue.append(currentNode.left)
            if currentNode.right is not None:
                myQueue.append(currentNode.right)
        return values


    # -- BFS End --
    def DFSPreOrder(self):
        values = []

        def traverse(currentNode: Node):

            values.append(currentNode.val)

            if currentNode.left is not None:
                traverse(currentNode.left)
        
            if currentNode.right is not None:
                traverse(currentNode.right)

        traverse(self.root)
        return values

    
    def DFSInOrder(self):
        values = []

        def traverse(currentNode: Node):

            if currentNode.left is not None:
                traverse(currentNode.left)

            values.append(currentNode.val)
        
            if currentNode.right is not None:
                traverse(currentNode.right)

        traverse(self.root)
        return values

    def DFSPostOrder(self):
        values = []

        def traverse(currentNode: Node):

            if currentNode.left is not None:
                traverse(currentNode.left)

            if currentNode.right is not None:
                traverse(currentNode.right)

            values.append(currentNode.val)

        traverse(self.root)
        return values

# -- BinarySearchTree End --




myTree = BinarySearchTree()
myTree.insert(38)   # root

myTree.insert(19)   # root.left
myTree.insert(69)   # root.right

myTree.insert(12)   # root.left.left
myTree.insert(24)   # root.left.right

myTree.insert(59)   # root.right.left
myTree.insert(95)   # root.right.right

print()

print("BFS:")
print(myTree.BFS())

print("DFSPreOrder:")
print(myTree.DFSPreOrder())

print("DFSInOrder:")
print(myTree.DFSInOrder())

print("DFSPostOrder:")
print(myTree.DFSPostOrder())

print()