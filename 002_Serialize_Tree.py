#This problem was asked by Google.
#Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, 
#and deserialize(s), which deserializes the string back into the tree.
#For example, given the following Node class
#class Node:
#    def __init__(self, val, left=None, right=None):
#        self.val = val
#        self.left = left
#        self.right = right
#The following test should pass:
#node = Node('root', Node('left', Node('left.left')), Node('right'))
#assert deserialize(serialize(node)).left.left.val == 'left.left'

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def add_node(node, string) :
    string += node.val
    if (node.left or node.right) :
        string += ":"
        if (node.left) : 
            string = add_node(node.left, string)
        string += ","
        if (node.right) :
            string = add_node(node.right, string)
    return string

def serialize(root) :
    string = ""
    add_node(root, string)
    return string

if __name__ == "__main__" : 
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    print(serialize(node))