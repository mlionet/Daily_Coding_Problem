#This problem was asked by Google.
#A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
#Given the root to a binary tree, count the number of unival subtrees.
#For example, the following tree has 5 unival subtrees:
#   0
#  / \
# 1   0
#    / \
#   1   0
#  / \
# 1   1

class Node:
    def __init__(self, val, left=None, right=None) :
        self.val = val
        self.left = left
        self.right = right

def is_unival(node):
    if node == None :
        return True
    if node.left != None and node.left.val != node.val :
        return False
    if node.right != None and node.right.val != node.val :
        return False
    return is_unival(node.left) and is_unival(node.right)

def count_unival_subtrees(node) :
    if (node == None) :
        return 0
    is_uni = 1 if is_unival(node) else 0
    return is_uni + count_unival_subtrees(node.left) + count_unival_subtrees(node.right)

##----TEST ZONE----##

if __name__ == "__main__" : 
    #INTERVIEW TEST

    node = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0))) 
    print(count_unival_subtrees(node)) #Should give 5
    #MY TEST
    node = Node(0, Node(0), Node(0))
    print(count_unival_subtrees(node)) #Should give 3
    node = Node(0, Node(1), Node(0))
    print(count_unival_subtrees(node)) #Should give 2
    node = Node(1, Node(1, Node(1), Node(1)), Node(1, Node(1), Node(1))) 
    print(count_unival_subtrees(node)) #Should give 7
    node = None
    print(count_unival_subtrees(node)) #Should give 0
