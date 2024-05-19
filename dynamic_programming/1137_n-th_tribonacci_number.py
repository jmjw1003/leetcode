class Solution:
    def tribonacci(self, n: int) -> int:
        t = [0, 1, 1]
        if n < 3:
            return t[n]
        
        for i in range(3, n + 1):
            t[0], t[1], t[2] = t[1], t[2], t[0] + t[1] + t[2]
        
        return t[-1]
    

"""
Can also be solved with recursion and memoization:

from functools import cache


class Solution:
    @cache
    def tribonacci(self, n: int) -> int:
        if n  < 1:
            return 0
        if n < 3:
            return 1
        return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
"""