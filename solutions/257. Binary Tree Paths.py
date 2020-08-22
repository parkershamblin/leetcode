# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root):
        self.res = []
        self.helper(root, "")
        return self.res
    
    def helper(self, root, path):
        if root:
            path += f"{str(root.val)}->"
            self.helper(root.left, path)
            self.helper(root.right, path)
            if not root.left and not root.right:
                self.res.append(path[:-2])
