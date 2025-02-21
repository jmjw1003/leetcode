# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    """Lazy iterator, saves on memory"""
    def _populate_stack(self, current_node):
        while current_node:
            self.stack.append(current_node)
            current_node = current_node.left

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self._populate_stack(root)

    def next(self) -> int:
        next_node = self.stack.pop()
        self._populate_stack(next_node.right)
        return next_node.val

    def hasNext(self) -> bool:
        return True if self.stack else False


class BSTIterator2:
    """Pre-processed tree"""
    def _traverse_tree(self, node):
        if node.left:
            self._traverse_tree(node.left)
        self.node_values.append(node.val)
        if node.right:
            self._traverse_tree(node.right)

    def __init__(self, root: Optional[TreeNode]):
        self.node_values = []
        if root:
            self._traverse_tree(root)
        self.ptr = 0

    def next(self) -> int:
        self.ptr += 1
        return self.node_values[self.ptr - 1]

    def hasNext(self) -> bool:
        return self.ptr < len(self.node_values)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()