class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set(["a", "e", "i", "o", "u"])
        word = list(s)
        l, r = 0, len(word) - 1
        while l < r:
            if word[l].lower() not in vowels:
                l += 1
            elif word[r].lower() not in vowels:
                r -= 1
            else:
                word[l], word[r] = word[r], word[l]
                l += 1
                r -= 1
        return "".join(word)