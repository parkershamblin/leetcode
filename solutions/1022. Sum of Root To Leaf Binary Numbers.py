# hint add an extra parameter and use the LSB to MSB trick (val = val * 2 + root.val) [Delete after first solved]
# [do not look at notes unless you want spoiler]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode, val=0) -> int:
        if not root:
            return 0  # 0 or val
        val = val * 2 + root.val
        if not root.left and not root.right:
            return val
        return self.sumRootToLeaf(root.left, val) + self.sumRootToLeaf(root.right, val)