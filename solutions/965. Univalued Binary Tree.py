# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        stack = [root]
        while stack:
            tmp = stack.pop()
            if tmp.val != root.val:
                return False
            tmp_children = []
            for child in [tmp.left, tmp.right]:
                if child:
                    tmp_children.append(child)
            for child in tmp_children[::-1]:
                stack.append(child)
        return True