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


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        """Iterative solution"""
        node_values = []
        stack = []
        curr_node = root
        while curr_node or stack:
            while curr_node:
                stack.append(curr_node)
                curr_node = curr_node.left
            curr_node = stack.pop()
            node_values.append(curr_node.val)
            curr_node = curr_node.right

        return node_values