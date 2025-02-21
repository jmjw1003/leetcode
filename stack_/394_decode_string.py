class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char != "]":
                stack.append(char)
            else:
                substring = ""
                factor = ""
                while stack[-1] != "[":
                    char = stack.pop()
                    substring = char + substring
                stack.pop()  # [
                while stack and stack[-1].isdigit():
                    digit = stack.pop()
                    factor = digit + factor
                stack.append(int(factor) * substring)
        return "".join(stack)
