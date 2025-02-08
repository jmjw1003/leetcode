import random

class RandomizedSet:
    def __init__(self):
        """
        In order for constant time operations a hashmap is required to keep track
        of indexes of values in the array.
        """
        self.value_map = {}
        self.set_values = []

    def insert(self, val: int) -> bool:
        """Append to the end of the array, track index"""
        insert = val not in self.value_map
        if insert:
            idx = len(self.set_values)
            self.value_map[val] = idx
            self.set_values.append(val)
        return insert

    def remove(self, val: int) -> bool:
        """In order to maintain value -> index relationship, swap the element being
        removed and the last element of the array, update map for the swapped value
        and delete the element being removed."""
        delete = val in self.value_map
        if delete:
            idx = self.value_map[val]
            last = self.set_values[-1]
            self.value_map[last] = idx
            self.set_values[idx] = last
            del self.value_map[val]
            self.set_values.pop()
        return delete

    def getRandom(self) -> int:
        """Constraint that there will be at least one element present when this 
        method is called allows for random.choice"""
        return random.choice(self.set_values)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()