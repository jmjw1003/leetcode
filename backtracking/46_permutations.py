class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        # Base case
        if len(nums) == 0:
            return [[]]

        output = []
        # Get all permutations for nums without first element
        perms = self.permute(nums[1:])
        for perm in perms:
            # For each permutation, insert first element in every possible position
            for i in range(len(perm) + 1):
                p = perm.copy()     
                p.insert(i, nums[0])
                output.append(p)

        return output
