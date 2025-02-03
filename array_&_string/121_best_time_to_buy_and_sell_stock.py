class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0  # Max profit lower bound
        buy = prices[0] # Set inital buy price
        # Iterate through prices
        for price in prices:
            # Update buy price if lower than current buy price
            if price < buy:
                buy = price
            # Else, calculate sale price & update max_profit
            else:
                max_profit = max(price - buy, max_profit)
        return max_profit
