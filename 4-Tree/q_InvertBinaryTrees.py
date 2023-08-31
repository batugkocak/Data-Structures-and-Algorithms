class Node():
    def __init__(self, val) -> None:
        self.val = val
        self.right = None
        self.left = None

def invertTree(self, root):
    #exit condition
    if root is None:
        return None
    root.left, root.right = root.right, root.left

    invertTree(root.left)
    invertTree(root.right)

    return root
