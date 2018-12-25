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

#How i serialize : "root:{left:{left.left,left.right},right:{right.left, right.right}}"

def serialize(node) :
    string = node.val
    if (node.left or node.right) :
        string += ":{"
        if (node.left) : 
            string += serialize(node.left)
        string += ","
        if (node.right) :
            string += serialize(node.right)
        string += "}"
    return string

#Returns the left child and right child of the node
def split_right_left(string):
    count = 0
    i = 0
    while i < len(string) :
        if string[i] == '{' : count += 1
        if string[i] == '}' : count -= 1
        if string[i] == ',' and count == 1 :
            left = string[1 : (i)]
            right = string[(i + 1) : len(string) - 1]
        i += 1
    return left, right

def deserialize(string) :
    if len(string) == 0 : return None
    split = string.split(':', 1)
    node = Node(split[0])
    if len(split) > 1 :
        left, right = split_right_left(split[1])
        node.right = deserialize(right)
        node.left = deserialize(left)
    return node

##----TEST ZONE----##

if __name__ == "__main__" : 
    #INTERVIEW TEST
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node)).left.left.val == 'left.left'
    #MY TEST
    node = Node('root', Node('left', Node('left.left'), Node('left.right')), Node('right', Node('right.left'), Node('right.right')))
    serie_original = serialize(node)
    print("original serie = " + serie_original)
    node_new = deserialize(serie_original)
    serie_new = serialize(node_new)
    print("new serie      = " + serie_new)
    print(serie_original == serie_new)
