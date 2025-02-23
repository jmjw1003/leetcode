# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """Preorder: node, left, right"""
        if not root:
            return []
        
        def traverse(node, node_values):
            node_values.append(node.val)
            if node.left:
                traverse(node.left, node_values)
            if node.right:
                traverse(node.right, node_values)

        node_values = []
        traverse(root, node_values)

        return node_values

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """Iterative solution."""
        node_values = []
        stack = []
        current_node = root
        while current_node or stack:
            if current_node:
                node_values.append(current_node.val)
                if current_node.right:
                    stack.append(current_node.right)
                current_node = current_node.left
            else:
                current_node = stack.pop()

        return node_values