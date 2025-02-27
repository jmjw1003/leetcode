class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        
        steps = [2, 1]

        for step in range(3, n + 1):
            steps[0], steps[1] = steps[0] + steps[1], steps[0]
        
        return steps[0]
