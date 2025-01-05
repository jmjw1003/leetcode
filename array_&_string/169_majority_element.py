class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # Time: O(nlog(n)), space O(1) ezpz method
        # nums.sort()
        # return nums[len(nums) // 2]

        # Time O(n), space O(n)
        seen = {}
        majority = (len(nums) // 2) + 1

        for num in nums:
            count = seen.get(num, 0) + 1
            if count >= majority:
                return num
            seen[num] = count

        # Apparently there is a Boyer-Moore Voting Algorithm that can solve this in O(n) time and O(1) space
        # but there is zero chance I would have come up with that on my own