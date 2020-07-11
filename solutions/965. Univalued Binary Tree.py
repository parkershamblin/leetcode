# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        stack = [root]
        value = root.val
        res = []
        while stack:
            tmp =  stack.pop()
            if tmp.val != value:
                return False
            res.append(tmp.val)
            tmp_children = []
            if tmp.left:
                tmp_children.append(tmp.left)
            if tmp.right:
                tmp_children.append(tmp.right)
            for child in tmp_children[::-1]:
                stack.append(child)
        return True