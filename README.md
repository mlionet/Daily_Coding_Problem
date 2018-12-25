# Daily Coding Problem
### Interview problems solved in python !

#### 001 - This problem was asked by Stripe
>Given an array of integers, find the first missing positive integer in linear time and constant space.  
>In other words, find the lowest positive integer that does not exist in the array.  
>The array can contain duplicates and negative numbers as well.  
>For example, the input __[3, 4, -1, 1]__ should give 2. The input __[1, 2, 0]__ should give 3.  
>You can modify the input array in-place.

#### 002 - This problem was asked by Google
>Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s),  
>which >deserializes the string back into the tree. For example, given the following Node class :
```
class Node:  
  def __init__(self, val, left=None, right=None):  
    self.val = val  
    self.left = left  
    self.right = right
```
>The following test should pass:  
```
node = Node('root', Node('left', Node('left.left')), Node('right'))  
assert deserialize(serialize(node)).left.left.val == 'left.left'
```
