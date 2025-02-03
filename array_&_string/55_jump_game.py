class Solution:
    def canJump(self, nums: list[int]) -> bool:
        target = len(nums) - 1 # Current goal: reach last index

        # Iterate backwards through the array starting at second last index
        for idx in range(target - 1, -1, -1):
            # Calculate how far we can move from this index
            max_distance = idx + nums[idx]
            # If we can reach the goal from here, this becomes the new target
            if max_distance >= target:
                target = idx

        # If the target has reached the first element in the array we can reach the last index
        return target == 0