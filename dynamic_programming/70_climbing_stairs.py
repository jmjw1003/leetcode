class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1, 1]
        for i in range(n - 1):
            val = dp[-1] + dp[-2]
            dp.append(val)
        return dp[-1]
    
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        for i in range(n - 1):
            one, two = one + two, one
        return one