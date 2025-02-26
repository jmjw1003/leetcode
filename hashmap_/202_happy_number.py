class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n not in seen:
            seen.add(n)
            new_val = 0
            for digit in str(n):
                val = (int(digit) ** 2)
                new_val += val
            if new_val == 1:
                return True
            n = new_val

        return False
