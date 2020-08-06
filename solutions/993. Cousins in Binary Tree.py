# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
​
​
from collections import namedtuple
NodeAttributes = namedtuple('NodeAttributes', ['parent', 'depth'])
​
​
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        lookup = {}
        
        stack = [(root, None, 0)]
        while stack:
            node, parent, depth = stack.pop()
            if node and node.val in (x, y):
                lookup[node.val] = NodeAttributes(parent, depth)
            if node.left:
                stack.append((node.left, node, depth + 1))
            if node.right:
                stack.append((node.right, node, depth + 1))
        
        return lookup[x].parent != lookup[y].parent and lookup[x].depth == lookup[y].depth
