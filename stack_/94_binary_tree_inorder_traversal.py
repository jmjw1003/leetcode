# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """In order traversal: left, val, right"""
        if not root:
            return []

        def traverse(node, node_values):
            if node.left:
                traverse(node.left, node_values)
            node_values.append(node.val)
            if node.right:
                traverse(node.right, node_values)

        node_values = []
        traverse(root, node_values)

        return node_values
