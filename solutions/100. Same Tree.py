# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        p_values, q_values = [], []
        self.dfs(p, p_values)
        self.dfs(q, q_values)
        return all(v1 == v2 for v1, v2 in zip(p_values, q_values))
    
    def dfs(self, node: TreeNode, values):
        # preorder dfs
        if not node:
            values.append(None)
        else:
            values.append(node.val)
            self.dfs(node.left, values)
            self.dfs(node.right, values)
