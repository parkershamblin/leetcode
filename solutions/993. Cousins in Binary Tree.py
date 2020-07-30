# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
​
from collections import namedtuple
NodeAttributes = namedtuple('NodeAttributes', ['depth', 'parent'])
​
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        lookup = {}
        stack = [(root, 0, None)]
​
        while stack:
            node, depth, parent = stack.pop()
            if node.val in (x, y):
                lookup[node.val] = NodeAttributes(depth, parent)
            if node.left:
                stack.append((node.left, depth+1, node.val))
            if node.right:
                stack.append((node.right, depth+1, node.val))
​
        if lookup[x].depth == lookup[y].depth and lookup[x].parent != lookup[y].parent:
            return True
