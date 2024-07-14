# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        stack = deque([root])
        level = 0
        max_sum = root.val
        max_level = 1
        while stack:
            sum_ = 0
            level += 1
            for i in range(len(stack)):
                node = stack.popleft()
                sum_ += node.val
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            if sum_ > max_sum:
                max_sum = sum_
                max_level = level
        return max_level

