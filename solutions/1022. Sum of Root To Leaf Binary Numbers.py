# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        res = []
        self.helper(root, path=0, res=res)
        return sum(res)
​
    def helper(self, root: TreeNode, path: int, res: list) -> None:
        if not root:
            return None
        path = 2 * path + root.val
        if not root.left and not root.right:
            res.append(path)
        self.helper(root.left, path, res)
        self.helper(root.right, path, res)
        
