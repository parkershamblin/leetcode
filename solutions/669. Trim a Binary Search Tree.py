# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        if not root:
            return
        # if root.val is less than L cut off then abonden left subtree and trim right subtree
        elif L > root.val:
            return self.trimBST(root.right, L, R)
        # if root.val is more than R cut off then aboden right sub tree and trim left sub tree
        elif R < root.val:
            return self.trimBST(root.left, L, R)
        # else recursively trim left and right sub trees
        root.left = self.trimBST(root.left, L, R)
        root.right = self.trimBST(root.right, L, R)
        return root
