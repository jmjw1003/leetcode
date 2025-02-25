class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        """Time: O(nlogn), space: O(1)"""
        nums.sort()
        l, r = 0, len(nums) - 1
        max_operations = 0
        while l < r:
            if nums[l] + nums[r] == k:
                max_operations += 1
                l += 1
                r -= 1
            elif nums[l] + nums[r] < k:
                l += 1
            else:
                r -= 1
        
        return max_operations

    def maxOperations(self, nums: list[int], k: int) -> int:
        """Time: O(n), space: O(n)"""
        frequency = {}
        max_operations = 0

        for n in nums:
            if frequency.get(k - n, 0) > 0:
                max_operations += 1
                frequency[k - n] -= 1
            else:
                frequency[n] = frequency.get(n, 0) + 1

        return max_operations
    