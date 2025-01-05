class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k = k % length
        n = length - k
        nums[n:], nums[:n] = nums[:n], nums[n:]
