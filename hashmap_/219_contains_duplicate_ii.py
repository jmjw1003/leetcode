class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        last_index = {}
        
        for i, num in enumerate(nums):
            if num in last_index and abs(last_index[num] - i) <= k:
                return True
            last_index[num] = i

        return False
