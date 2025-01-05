class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        removals = 0
        for i in range(len(nums)):
            idx = i - removals
            if nums[idx] == val:
                removals += 1
                del nums[idx]