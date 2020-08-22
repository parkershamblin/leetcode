"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
​
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result = []
        queue = collections.deque([root])
        while queue:
            node = queue.pop()
            if node:
                if node.children:
                    for child in node.children:
                        queue.append(child)
                if not node.children:
                    result.append(node.val)
                else:
                    result.append(node.val)
        
        return result[::-1]
​
