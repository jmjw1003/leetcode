# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # Upper and lower bounds
        lower, upper = 1, n

        while True:
            pick = (upper + lower) // 2
            result = guess(pick)
            if result == 0:
                return pick
            elif result == -1:
                upper = pick - 1
            else:
                lower = pick + 1