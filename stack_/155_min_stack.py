class MinStack:
    def __init__(self):
        self.stack = []  # Contains value, min_value @ this point in the stack

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append([val, val])
        else:
            curr_min = self.stack[-1][-1]
            new_min = min(val, curr_min)
            self.stack.append([val, new_min])
        
    def pop(self) -> None:
        self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()