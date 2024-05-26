class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_consecutive_ones = 0
        flips = left = 0
        for right in range(len(nums)):
            flips += 1 - nums[right]

            while flips > k:
                flips -= 1 - nums[left]
                left += 1
            
            consecutive_ones = right - left + 1
            max_consecutive_ones = max(max_consecutive_ones, consecutive_ones)
        
        return max_consecutive_ones
