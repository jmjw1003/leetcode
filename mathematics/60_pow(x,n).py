class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return float(1)
        if x == 0:
            return float(0)
        
        if n < 0:
            n *= -1
            x = 1 / x
        
        def helper(x, n):
            if n == 0: return 1
            if x == 0: return 0

            res = helper(x, n // 2)
            res = res * res
            return res * x if n % 2 else res

        res = helper(x, n)
        return res
