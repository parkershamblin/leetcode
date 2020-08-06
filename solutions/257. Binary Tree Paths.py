# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = []
        self.dfs(root, path="", res=res)
        return res
        
        
    def dfs(self, node, path, res):
        # preorder
        if not node:
            return None
        path += f"{str(node.val)}->"
        if not node.left and not node.right:
            res.append(path[:-2])
        self.dfs(node.left, path, res)
        self.dfs(node.right, path, res)
