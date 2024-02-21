ArrayNodes = [[-1] * 3 for i in range(20)]

FreeNode = 6
RootPointer = 0

def search_value(root, value_to_find, array_nodes):
    if root == -1:
        return -1
    else:
        if array_nodes[root][1] == value_to_find:
            return root
        else:
             if array_nodes[root][1] == -1:
                 return -1
    if array_nodes[root][1] < value_to_find:
        return search_value(array_nodes[root][0], value_to_find, array_nodes)
    if array_nodes[root][1] > value_to_find:
        return search_value(array_nodes[root][2], value_to_find, array_nodes)
    
def post_order(root):
    if root is not None:

        post_order(root.left)
        post_order(root.right)
        print(root.value)

result = search_value(0, 15, ArrayNodes)
if result != -1:
    print(f"Value 15 found at index {result}")
else:
    print("Value 15 not found in the tree")

post_order(0, ArrayNodes)


