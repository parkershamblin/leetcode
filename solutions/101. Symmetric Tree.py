# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        queue = [root]
​
        while root and queue:
            lqueue = [node.left for node in queue]
            rqueue = [node.right for node in queue]
            
            if ([node.val if node else None for node in reversed(lqueue)] != 
                  [node.val if node else None for node in rqueue]):
                return False
            else:
                queue = [child for node in queue for child in (node.left, node.right) if child]
​
        return True
