# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        stack = deque([root])
        res = []
        while stack:
            for i in range(len(stack)):
                node = stack.popleft()
                if node:
                    right_most_value = node.val
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            res.append(right_most_value)
        return res