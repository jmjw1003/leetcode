class Solution:
    def candy(self, ratings: list[int]) -> int:
        length = len(ratings)
        candies = [1] * length

        for idx in range(1, length):
            if ratings[idx] > ratings[idx - 1]:
                candies[idx] = candies[idx - 1] + 1

        for idx in range(length-2, -1, -1):
            if ratings[idx] > ratings[idx + 1]:
                # Already done one pass, may already be greater than right neighbour
                candies[idx] = max(candies[idx], candies[idx  + 1] + 1)

        return sum(candies) 