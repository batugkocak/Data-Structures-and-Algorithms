def convertBST(root):
    sumOfValues= 0 

    def traversal(node):

        if node.left is not None: 
            traversal(node.left)
        
        temp = node.val
        node.val += sumOfValues
        sumOfValues += temp     

        if node.right is not None:
            traversal(node.left)
        
