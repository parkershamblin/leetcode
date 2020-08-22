# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        """For Two Trees to be the Same:
        - node1.val must equal node2.val
        - node1's left subtree must match node2's left subtree
        - node1's right subtree must match node2's right subtree
        """
        return self.dfs(p, q)
​
    def dfs(self, node1, node2):
        if not node1 and not node2:
            return True
        elif not node1 or not node2:
            return False
        
        return (
            node1.val == node2.val
            and self.dfs(node1.left, node2.left)
            and self.dfs(node1.right, node2.right)
        )
