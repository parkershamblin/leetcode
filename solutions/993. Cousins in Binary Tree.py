# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        # intentionally taking BFS approach this time
        # x.depth == y.depth & x.parent != y.parent
        queue = [root]
        while queue and root:
            tmp = [child.val for parent in queue for child in (parent.left, parent.right) if child]
            x_parent, y_parent = None, None
            if x in tmp and y in tmp:
                parents = {}
                for parent in queue:
                    for child in (parent.left, parent.right):
                        if child:
                            if child.val == x:
                                x_parent = parent
                            elif child.val == y:
                                y_parent = parent
            if x_parent and y_parent:
                if x_parent != y_parent:
                    return True
            queue = [child for parent in queue for child in (parent.left, parent.right) if child]
​
