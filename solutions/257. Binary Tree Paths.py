# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = []
​
        def dfs(node, parent, path):
            if not node:
                return
​
            path = path + str(node.val) + "->"
​
            if not node.left and not node.right:
                return path[:-2]
​
            left = dfs(node.left, node, path)
            right = dfs(node.right, node, path)
​
            if left: res.append(left)
            if right: res.append(right)
        
        # edge case handling for root empty tree and root node with no left or right child
        if root:
            if not root.left and not root.right:
                return [f"{root.val}"]
​
        # kick off recursive function on root
        dfs(root, parent=None, path="")
        return res
