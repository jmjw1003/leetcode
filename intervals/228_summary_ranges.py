class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if not nums:
            return []
        summary_ranges = []
        curr_range = [nums[0], nums[0]]

        for idx in range(1, len(nums)):
            num = nums[idx]
            if num - 1 == curr_range[1]:
                curr_range[1] = num
            else:
                if curr_range[0] == curr_range[1]:
                    summary_ranges.append(str(curr_range[0]))
                else:
                    summary_ranges.append(f'{curr_range[0]}->{curr_range[1]}')
                curr_range = [num, num]

        if curr_range[0] == curr_range[1]:
            summary_ranges.append(str(curr_range[0]))
        else:
            summary_ranges.append(f'{curr_range[0]}->{curr_range[1]}')

        return summary_ranges
