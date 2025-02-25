class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        l = 0
        longest_substring = 0
        for r in range(len(s)):
            char = s[r]
            if char not in chars:
                chars.add(char)
                longest_substring = max(longest_substring, r + 1 - l)
            else:
                while l <= r:
                    if s[l] == s[r]:
                        l += 1
                        break
                    else:
                        chars.remove(s[l])
                        l += 1

        return longest_substring
