"""
829. Consecutive Numbers Sum | Hard

Given an integer n, return the number of ways you can write n as the sum of consecutive positive integers.

Example 1:

Input: n = 5
Output: 2
Explanation: 5 = 2 + 3
Example 2:

Input: n = 9
Output: 3
Explanation: 9 = 4 + 5 = 2 + 3 + 4
Example 3:

Input: n = 15
Output: 4
Explanation: 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5
 

Constraints:

1 <= n <= 109
_____________________________________________________________________________________________________________
For each valid consecutive number sum, there will be a constant number added to an incrementing integer.
Checking if (constant % number of steps == 0) will verify if the number can be formed of
(number of steps) consecutive integers.

n = 15 is a good example to illustrate this point visually:

15 = (x + 1) => x = 14 % 1 == 0                                             : valid sum, increment output
15 = (x + 1) + (x + 2) => 2x = 12 % 2 == 0                                  : valid sum, increment output
15 = (x + 1) + (x + 2) + (x + 3) => 3x = 9 % 3 == 0                         : valid sum, increment output
15 = (x + 1) + (x + 2) + (x + 3) + (x + 4) => 5x = 5 % 4 != 0               : invalid sum
15 = (x + 1) + (x + 2) + (x + 3) + (x + 4) + (x + 5) => 6x = 0 % 5 == 0     : valid sum, increment output
15 = (x + 1) + (x + 2) + (x + 3) + (x + 4) + (x + 5) + (x + 6) => 7x < 0 => end loop


Solution uses O(1) space complexity, O(log(n)) time complexity.
"""

class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        N, i, output = n, 1, 0
        while N > 0:
            N -= i
            if N % i == 0:
                output += 1
            i += 1
        return output