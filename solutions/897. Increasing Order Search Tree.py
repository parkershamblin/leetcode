# Definition for a bindary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode, nodes: List=[]) -> TreeNode:
        nodes = []
        self.build_nodes(root, nodes)
        nodes2 = nodes[1:] + [None]
        for i in range(len(nodes)):
            nodes[i].left = None
            nodes[i].right = None
            if nodes2[i]:
                nodes2[i].left = None
            if nodes2[i]:
                nodes2[i].right = None
            nodes[i].right = nodes2[i]
        return nodes[0]
    def build_nodes(self, node, nodes):
        # inorder print root.val between recursive traversal of left and right subtree
        if node is None:
            return
        self.build_nodes(node.left, nodes)
        nodes.append(node)
        self.build_nodes(node.right, nodes)
