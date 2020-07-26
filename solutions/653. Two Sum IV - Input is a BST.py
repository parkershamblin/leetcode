# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        # UPDATE negative numbers are messing with my strat trying to utilize bst property
            # utilize bst property to efficiently solve
        # UPDATE CONTINUED now going to generate list of all values and just check if dif + val in there 
        values = []
        stack = [root]
        while stack:
            node = stack.pop()
            values.append(node.val)
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
​
        for v in values:
            dif = k - v
            if dif in values and dif != v:
                return True
        return False
