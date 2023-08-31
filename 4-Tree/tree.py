# Parent (Root) - Child (Parent) - Child (Leaf) Tree complexities are not linear, O ( log N), but there is also an
# idea that says its not O( log N), the worst scenario is O(N)
# So its theoretically O(N) but practically O( log N) [Unbalanced BTS is always O(N)]

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


myTree = BinarySearchTree()
print(myTree.insert(10))
print(myTree.insert(8))
print(myTree.insert(25))
print(myTree.insert(16))
print("Contains")
print(myTree.contains(16))
print(myTree.maxOfNode(myTree.root).val)
print(myTree.minOfNode(myTree.root).val)
