class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        # Edge case
        if len(nums) == 1:
            return 0

        # Initialise left & right pointers
        l, r = 0, len(nums) - 1
        # Check boundaries
        if nums[l] > nums[l+1]:
            return l
        if nums[r] > nums[r-1]:
            return r
        # Binary search for a peak
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] < nums[mid + 1]:
                l = mid + 1
            else:
                r = mid - 1
