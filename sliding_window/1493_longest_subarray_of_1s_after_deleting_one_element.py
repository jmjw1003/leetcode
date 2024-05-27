class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = zeros = max_subarray = 0
        for r in range(len(nums)):
            # check if 1 or 0
            zeros += 1 - nums[r]
            
            # check if valid window
            while zeros > 1:
                zeros -= 1 - nums[l]
                l += 1
            
            # record current window length
            curr_subarray = r - l # == r - l + 1 - 1
            max_subarray = max(curr_subarray, max_subarray)
        
        return max_subarray