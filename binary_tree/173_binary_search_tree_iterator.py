# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:
    def _populate_stack(self, current_node):
        while current_node:
            self.stack.append(current_node)
            current_node = current_node.left

    def __init__(self, root: TreeNode | None = None):
        self.stack = []
        self._populate_stack(root)

    def next(self) -> int:
        next_node = self.stack.pop()
        self._populate_stack(next_node.right)
        return next_node.val

    def hasNext(self) -> bool:
        return True if self.stack else False
        

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()