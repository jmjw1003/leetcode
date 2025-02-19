class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {
            "}": "{",
            ")": "(",
            "]": "["
        }
        for char in s:
            # Opening bracket
            if char not in hashmap:
                stack.append(char)
            # Closing bracket
            else:
                # Check if stack exists or last element is matching open bracket
                if not stack or stack[-1] != hashmap[char]:
                    return False
                # If matching, pop the matching bracket
                stack.pop()
        
        # If there is a remaining stack it must contain an unmatched opening bracket
        return not stack
