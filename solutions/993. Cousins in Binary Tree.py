# 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        # return True if node1.depth = node2.depth and node1.parent != node2.parent
        # traverse the tree level by level
        current_level = [root]
        while current_level:
            next_level = []
            for node in current_level:
                if node.left: next_level.append((node.left, node.val))  # (node, parent)
                if node.right: next_level.append((node.right, node.val))
                if x in [node[0].val for node in next_level if node[0]]:
                    if y in [node[0].val for node in next_level if node[0]]:
                        for i, node in enumerate(next_level):
                            if node[0].val == x:
                                x_parent = node[1]
                            elif node[0].val == y:
                                y_parent = node[1]
                        if x_parent != y_parent:
                            return True
            current_level = [node[0] for node in next_level]
            next_level = []
        return False
