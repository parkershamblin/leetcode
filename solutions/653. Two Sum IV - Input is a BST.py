"""
notes
# inorder, preorder, postorder, levelorder?
# anyway avoid duplicate comparisons?
# is eveyr root id unique? (yes)
# anyway to utilize nature of BST to make less comparisons? (speed up solution)

ideas
# if the node.val is greater than or equal to the target than I don't need to search any further down that subtree's right path. (nevermind. this is not true because node values can be negative and so can target)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        # just going to write a brute force solution first
        result = []
        stack = [root]
        basket = []
        while stack:
            node = stack.pop()
            if node:
                basket.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        for n in basket:
            dif = k - n
            # i can do this since BST has all unique values
            if dif in basket and dif != n:
                return True
        # return False if dif is never found in basket
        return False