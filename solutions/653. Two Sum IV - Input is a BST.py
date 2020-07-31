# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        values = []
        return self.dfs_preorder(root, k, values)
    def dfs_preorder(self, root: TreeNode, k: int, values: list) -> bool:
        # preorder prints root.val before recursive traversally of left and right subtree.
        
        # 1. print root.val
        if root is None:
            return
        if k - root.val in values:
            return True
        else:
            values.append(root.val)
        
        # 2. recursive traversal of left subtree
        if self.dfs_preorder(root.left, k, values):
            return True
        
        # 3. recursive traversal of right subtree
        if self.dfs_preorder(root.right, k, values):
            return True
