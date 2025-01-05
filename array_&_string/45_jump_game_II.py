class Solution:
    def jump(self, nums: list[int]) -> int:
        res = 0
        l, r = 0, 0  # used to created "window" for BFS, always starting at first index

        while r < len(nums) - 1:  # ensures we can reach the final index of the array
            farthest_jump = 0
            for idx in range(l, r + 1):
                farthest_jump = max(farthest_jump, idx + nums[idx])
            l = r + 1
            r = farthest_jump
            res += 1
        
        return res