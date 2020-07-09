# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 == None and t2 == None:
            return None
        elif t1 and t2 == None:
            return t1
        elif t1 == None and t2:
            return t2
        else:
            merged_node = TreeNode(t1.val + t2.val)
            merged_node.left = self.mergeTrees(t1.left, t2.left)
            merged_node.right = self.mergeTrees(t1.right, t2.right)
            return merged_node