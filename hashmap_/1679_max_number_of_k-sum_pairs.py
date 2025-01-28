class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        max_operations = 0
        seen_nums = {}

        for num in nums:
            remainder = k - num
            if seen_nums.get(remainder, 0) > 0:
                max_operations += 1
                seen_nums[remainder] -= 1
            else:
                seen_nums[num] = seen_nums.get(num, 0) + 1

        return max_operations
