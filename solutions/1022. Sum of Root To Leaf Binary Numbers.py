# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode, val=0) -> int:
        res = []
        self.dfs_preorder(root, val, res)
        return sum(res)
            
    def dfs_preorder(self, root: TreeNode, val=0, res: list=[]) -> str:
        if root is None:
            return
        val = 2*val + root.val
        if root.left is None and root.right is None:
            res.append(val)
        if root.left:
            self.dfs_preorder(root.left, val, res)
        if root.right:
            self.dfs_preorder(root.right, val, res)
