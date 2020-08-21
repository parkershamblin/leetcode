# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.previous = -float('inf')
        self.result = float('inf')
​
    def getMinimumDifference(self, root: TreeNode) -> int:
        # the minimum difference will be between two adjacent nodes
        # inorder - visit root node in between recursive traversal of left and right subtree
        if root.left:
            self.getMinimumDifference(root.left)
        self.result = min(self.result, root.val - self.previous)
        self.previous = root.val
        if root.right:
            self.getMinimumDifference(root.right)
        return self.result
​
