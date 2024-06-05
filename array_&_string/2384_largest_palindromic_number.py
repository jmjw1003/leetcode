class Solution:
    def largestPalindromic(self, num: str) -> str:
        """
        Someone thought they were clever by adding a comically large number of 0s to one of the test cases
        so using bitwise operations speeds things up dramatically over conventional division and modulo operations.
        Took 31ms on leetcode, beating 99.94% (presumably most optimal possible solution).
        """

        lhs = ""                    # left-hand side
        mid = ""                    # middle (duh)
        rhs = ""                    # right-hand side
        inc = 0                     # flag to include the left & right sides

        c = num.count('0')          # Count the number of zeros
        c_ = (c & 1)                # Check if the number of zeros is odd
        c = (c - c_) >> 1           # Floor divide the number of zeros by 2 
        lhs += '0' * c              # Add half the zeros to the left-hand side
        rhs += '0' * c              # Add half the zeros to the right-hand side
        if c_:
            mid = '0'               # If the number of zeros is odd, add a zero to the middle

        for i in "123456789":
            c = num.count(i)        # Get the count of the current digit
            c_ = (c & 1)            # Check if the count is odd
            c = (c - c_) >> 1       # Floor divide the count by 2
            s = i * c               # Multiply the digit by the count
            lhs = s + lhs           # Add the digit to the left-hand side
            rhs += s                # Add the digit to the right-hand side
            if c_:
                mid = i             # If the count is odd, set the middle digit
            inc = (c >= 1) | inc    # If a non-zero digit count is found, set the flag to include the left & right sides

        s = lhs * inc + mid + rhs * inc # Create output string
        
        return s if s else "0"      # Return output string if it exists else "0" (case when there are only an even number of zeros)


    def largestPalindromic_(self, num: str) -> str:
        """
        This is probably what I would write in an interview and is (probably) readable by humans.
        Took 50ms, beating 97.78%, so actually still pretty fast.
        """
        left = ""
        middle = ""
        right = ""
        include_sides = 0

        zero_count = num.count('0')
        if zero_count % 2 == 1:
            middle = '0'
        zero_pairs = zero_count // 2
        left += '0' * zero_pairs
        right += '0' * zero_pairs

        for i in "123456789":
            i_count = num.count(i)
            i_pairs = i_count // 2
            if i_count % 2 == 1:
                middle = i
            left = i * i_pairs + left
            right += i * i_pairs
            if i_pairs > 0:
                include_sides = 1
        

        result = left * include_sides + middle + right * include_sides

        return result if result else "0"
