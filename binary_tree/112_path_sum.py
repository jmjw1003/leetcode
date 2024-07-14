# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, currentSum):
            # Check node exists
            if not node:
                return False

            # Add node value to current sum
            currentSum += node.val

            # If leaf node, return if target reached
            if not node.left and not node.right:
                return currentSum == targetSum

            # Else run on children
            return dfs(node.left, currentSum) or dfs(node.right, currentSum)

        return dfs(root, 0)