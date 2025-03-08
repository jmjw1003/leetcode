from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        paths = []
        def dfs(node, currentPath, currentSum):
            if not node:
                return

            currentSum += node.val
            newPath = currentPath + [node.val]
            if not node.left and not node.right and currentSum == targetSum:
                paths.append(newPath)

            dfs(node.left, newPath, currentSum)
            dfs(node.right, newPath, currentSum)

        dfs(root, [], 0)
        return paths
