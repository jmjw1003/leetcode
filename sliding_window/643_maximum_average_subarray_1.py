class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if k == 1:
            return max(nums)
        
        window = nums[:k]
        current_sum = max_sum = sum(window)

        for i in range(k, len(nums)):
            current_sum -= nums[i - k]
            current_sum += nums[i]

            max_sum = max(max_sum, current_sum)

        return max_sum / k