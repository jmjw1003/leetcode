class Solution:
    def longestPalindrome(self, s: str) -> int:
        seen = set()
        result = 0
        for char in s:
            if char in seen:
                seen.remove(char)
                result += 2
            else:
                seen.add(char)
        
        if seen:
            result += 1

        return result