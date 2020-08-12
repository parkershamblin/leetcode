# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res, level = [], [root]
        while root and level:
            res.append([node.val for node in level])
            level = [child for node in level for child in (node.left, node.right) if child]
        return res
