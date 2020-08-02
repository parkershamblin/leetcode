# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        stack = [root]
        seen = set()
        
        while stack:
            node = stack.pop()
            if node:
                if k - node.val in seen:
                    return True
                else:
                    seen.add(node.val)
                stack.append(node.right)
                stack.append(node.left)
​