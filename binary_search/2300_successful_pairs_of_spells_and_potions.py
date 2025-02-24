class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        length = len(potions)
        successful_pairs = []
        for spell_power in spells:
            idx = length # index of lowest valid potion
            l, r = 0, length - 1
            while l <= r:
                mid = (l + r) // 2
                if (potions[mid] * spell_power) >= success:
                    idx = mid
                    r = mid - 1
                else:
                    l = mid + 1
            successful_pairs.append(length - idx)
        
        return successful_pairs