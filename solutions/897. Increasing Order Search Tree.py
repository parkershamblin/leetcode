# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = []
​
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.helper(root)
        for i, node in enumerate(self.result[:-1]):
            node.left = None
            node.right = self.result[i+1]
        return self.result[0]
​
    def helper(self, root: TreeNode) -> None:
        if root.left:
            self.helper(root.left)
        self.result.append(root)
        if root.right:
            self.helper(root.right)
