class Solution:
    def rob(self, nums: List[int]) -> int:
        rob_left = rob_right = 0
        # Always keep track of max from pervious two houses
        # [rob_left, rob_right, num, num + 1, ...]
        for num in nums:
            rob_left, rob_right = rob_right, max(rob_left + num, rob_right)
        return rob_right