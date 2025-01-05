class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        last_seen = [nums[0], 1]
        removed = 0
        for i in range(1, len(nums)):
            idx = i - removed
            if nums[idx] == last_seen[0]:
                times_seen = last_seen[1]
                if times_seen > 1:
                    removed += 1
                    del nums[idx]
                last_seen[1] = times_seen + 1
            else:
                last_seen = [nums[idx], 1]