# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        return self.get_leafs(root1) == self.get_leafs(root2)
        
    def get_leafs(self, root: TreeNode) -> list:
        stack = [root]
        leafs = []
        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            else:
                if not node.left and not node.right:
                    leafs.append(node.val)
        return leafs