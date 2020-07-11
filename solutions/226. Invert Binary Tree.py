# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # must swap all nodes .left and .right attributes
        stack = [root]
        while stack:
            u = stack.pop()
            if u:
                u.left, u.right = u.right, u.left
                for child in [u.left, u.right]:
                    stack.append(child)
        return root