class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        last_seen = nums[0]
        removed = 0
        for i in range(1, len(nums)):
            idx = i - removed
            if nums[idx] == last_seen:
                removed += 1
                del nums[idx]
            else:
                last_seen = nums[idx]