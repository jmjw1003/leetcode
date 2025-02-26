class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}

        for idx, num in enumerate(nums):
            remainder = target - num
            if remainder in seen:
                return[seen[remainder], idx]
            else:
                seen[num] = idx
