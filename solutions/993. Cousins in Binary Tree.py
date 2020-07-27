# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        found_nodes = []
        
        # passes in parent and depth to keep track of things
        def search(node: TreeNode, parent: TreeNode, depth: int):
            if node is None:
                return
            
            if node.val == x or node.val == y:
                found_nodes.append((depth, parent))
            
            search(node.left, node, depth+1)
            search(node.right, node, depth+1)
            
        # kick start recursive function on
        search(root, None, 0)
        return found_nodes[0][0] == found_nodes[1][0] and found_nodes[0][1] != found_nodes[1][1]
