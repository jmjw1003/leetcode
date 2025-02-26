class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(' ')
        if len(pattern) != len(s):
            return False
        char_map = {}
        word_set = set()
        for idx, char in enumerate(pattern):
            word = s[idx]
            if word in word_set and char not in char_map:
                return False
            if char in char_map and char_map[char] != word:
                return False
            char_map[char] = word
            word_set.add(word)

        return True
