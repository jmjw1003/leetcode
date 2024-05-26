class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels ="aeiou"
        letters = list(s)
        window = letters[:k]
        max_vowels = current_vowels = sum([1 for i in window if i in vowels])      

        for i in range(k, len(letters)):
            if letters[i - k] in vowels:
                current_vowels -= 1
            if letters[i] in vowels:
                current_vowels += 1
            max_vowels = max(max_vowels, current_vowels)
            if max_vowels == k:
                return k
        return max_vowels