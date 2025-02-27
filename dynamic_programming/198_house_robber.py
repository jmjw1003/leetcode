class Solution:
    def rob(self, nums: list[int]) -> int:
        rob_left = rob_right = 0
        # Always keep track of max from pervious two houses
        # [rob_left, rob_right, num, num + 1, ...]
        for num in nums:
            rob_left, rob_right = rob_right, max(rob_left + num, rob_right)
        return rob_right

class Solution:
    def rob(self, nums: list[int]) -> int:
        houses = len(nums)
        if houses < 3:
            return max(nums)
        
        totals = [nums[-2], nums[-1]]

        for house in range(houses - 3, -1, -1):
            totals[0], totals[1] = max(nums[house] + totals[1], totals[0]), max(totals[0], totals[1])
    
        return totals[0]
