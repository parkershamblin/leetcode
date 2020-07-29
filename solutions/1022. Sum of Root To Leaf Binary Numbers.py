# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def paths(root):
            if not root:
                return []
            if not root.left and not root.right:
                return [str(root.val)]
            return [str(root.val) + str(i) for i in paths(root.left)] + [str(root.val) + i for i in paths(root.right)]
        return sum(int(i, 2) for i in paths(root))
​
