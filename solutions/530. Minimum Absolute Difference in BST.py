# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    pre = -float('inf')
    res = float('inf')
    
    def getMinimumDifference(self, root: TreeNode) -> int:
        # minimum difference can only be between adjacent nodes
        # inorder
        if root.left:
            self.getMinimumDifference(root.left)
        self.res = min(self.res, root.val - self.pre)  # why does self.pre have to be negative infinity for this to work?
        self.pre = root.val
        if root.right:
            self.getMinimumDifference(root.right)
        return self.res
