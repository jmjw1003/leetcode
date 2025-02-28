from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.stack = []

    def populate_stack(self, node):
        self.stack.append(node)
        if node.left:
            self.populate_stack(node.left)
        if node.right:
            self.populate_stack(node.right)

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        self.populate_stack(root)

        curr = root
        for node in self.stack[1:]:
            curr.left = None
            curr.right = node
            curr = node
