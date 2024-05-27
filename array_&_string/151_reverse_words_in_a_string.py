class Solution:
    def reverseWords(self, s: str) -> str:
        l = [i for i in s.split(" ") if i][::-1]
        return " ".join(l)