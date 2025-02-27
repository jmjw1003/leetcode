class Node:
    # DLL node
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        # Create dummy nodes for DLL
        self.left, self.right = Node(0,0), Node(0,0)
        # Link them
        self.left.next, self.right.prev = self.right, self.left

    def insert(self, node: Node) -> None:
        prev = self.right.prev
        prev.next = self.right.prev = node
        node.prev, node.next = prev, self.right

    def remove(self, node: Node) -> None:
        prev, next_ = node.prev, node.next
        prev.next, next_.prev = next_, prev


    def get(self, key: int) -> int:
        if key in self.cache:
            # Fetch node
            node = self.cache[key]
            # Update node to MRU
            self.remove(node)
            self.insert(node)
            # Return value
            return node.val
        return -1
        

    def put(self, key: int, value: int) -> None:
        # Check if key exists
        if key in self.cache:
            # Fetch node to update value
            node = self.cache[key]
            node.val = value
            # Re-insert node as MRU
            self.remove(node)
            self.insert(node)
        else:
            # Create node
            node = Node(key, value)
            # Insert Node into cache and list
            self.cache[key] = node
            self.insert(node)
            # Check if capacity has been exceeded
            if len(self.cache) > self.capacity:
                # Find LRU node
                lru = self.left.next
                lru_key = lru.key
                # Remove from list
                self.remove(lru)
                # Remove from cache
                del self.cache[lru_key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)