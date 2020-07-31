# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = []
    
        def preorder(root, path):
            if not root:
                return ""
​
            path += f"{str(root.val)}->"
​
            if not root.left and not root.right:
                res.append(path[:-2])
    
            preorder(root.left, path)
            preorder(root.right, path)
        
        # kick off recursive call on root
        preorder(root, path="")
        return res
