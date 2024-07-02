class Solution:
    def removeStars(self, s: str) -> str:
        char_stack = []
        for char in s:
            if char != "*":
                char_stack.append(char)
            else:
                char_stack.pop()
        return "".join(char_stack)