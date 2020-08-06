# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return 0
        cur_level = [root]
        level_values = []
        while cur_level:
            next_level = []
            cur_level_values = []
            for node in cur_level:
                if node:
                    cur_level_values.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            level_values.append(cur_level_values)
            cur_level = next_level
        return [sum(level)/len(level) for level in level_values]
