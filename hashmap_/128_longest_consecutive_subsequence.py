class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        longest_consecutive = 0
        nums = set(nums)

        for num in nums:
            if (num - 1) in nums:
                continue
            
            consecutive_nums = 1
            while (num + 1) in nums:
                consecutive_nums += 1
                num += 1
            
            longest_consecutive = max(longest_consecutive, consecutive_nums)

        return longest_consecutive
