from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_count = Counter(magazine)
        ransome_note_count = Counter(ransomNote)

        for char, count in ransome_note_count.items():
            if magazine_count.get(char, 0) < count:
                return False
        
        return True
