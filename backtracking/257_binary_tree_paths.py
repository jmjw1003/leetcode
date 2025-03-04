from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        paths = []
        def backtrack(node, curr_path):
            curr_path += str(node.val)
            if not node.left and not node.right:
                paths.append(curr_path)
                return
            curr_path += "->"
            if node.left:
                backtrack(node.left, curr_path)
            if node.right:
                backtrack(node.right, curr_path)

        backtrack(root, "")

        return paths
