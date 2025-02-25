class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]  # 1-indexed array
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1
