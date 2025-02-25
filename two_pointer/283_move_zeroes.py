class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        z = 0 # zero pointer

        # non-zero pointer n
        for n in range(len(nums)):
            if nums[n] != 0:
                nums[z], nums[n] = nums[n], nums[z]
                z += 1
