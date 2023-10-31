class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)
IsFound = False
Search = input("Input something here")
for i in BinaryTree:
    if Search == BinaryTree[i]:
        print("Found")
        IsFound == True
    elif Search > BinaryTree[i]:
        IsFound == False