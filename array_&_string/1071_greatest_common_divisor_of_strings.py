class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)
        
        def isSubstring(l: int) -> bool:
            # Check if both strings can be divided by l
            if len1 % l or len2 % l:
                return False
            # Calculate factors
            f1, f2 = len1 // l, len2 // l # Need to be integer
            # Check if both strings are multiples of substring
            return str1[:l] * f1 == str1 and str1[:l] * f2 == str2
        
        """
        Working backwards from shorted string ensures we can just return the first match
        """
        for l in range(min(len1, len2), 0, -1):
            if isSubstring(l):
                return str1[:l]
        return ""