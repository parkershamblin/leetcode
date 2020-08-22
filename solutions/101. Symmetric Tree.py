# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.dfs(root, root)
    
    def dfs(self, node1, node2):
        if not node1 and not node2:
            return True
        elif not node1 or not node2:
            return False
        
        """A tree is symmetric if the left subtree is a mirror reflection of the right subtree.
        
        Therefore, the question is: when are two trees a mirror reflection of each other?
        
        Two trees are a mirror reflection of each other if:
        - Their two roots have the same value.
        - The right subtree of each tree is a mirror reflection of the left subtree of other tree.
        """
        return (
            node1.val == node2.val
            and self.dfs(node1.left, node2.right)
            and self.dfs(node1.right, node2.left)
        )
​
