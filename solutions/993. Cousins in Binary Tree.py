# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        lookup = {}
        stack = [(root, 0, None)]
        
        while stack:
            node, depth, parent = stack.pop()
            if node and node.val in (x, y):
                lookup[node.val] = (depth, parent)
            if node.right:
                stack.append((node.right, depth+1, node))
            if node.left:
                stack.append((node.left, depth+1, node))
        return lookup[x][0] == lookup[y][0] and lookup[x][1] != lookup[y][1]
