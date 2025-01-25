class Solution:
    def myAtoi(self, s: str) -> int:
        number_string = ""

        # Remove whitespace
        s = s.strip()

        # Make list
        s = list(s)
        
        # Get 32 bit signed in ranges
        umin = -2 ** 31
        umax = (2 ** 31) - 1

        # Iterate through s to find number
        while s:
            if s[0] == "+" and len(s) > 1 and s[1].isdigit() and not number_string:
                del s[0]
            elif s[0] == "-" and len(s) > 1 and s[1].isdigit() and not number_string:
                del s[0]
                number_string = "-"
            elif s[0].isdigit():
                number_string += s[0]
                del s[0]
            else:
                break
        
        # If loop broken and no number detected, default to 0
        if not number_string:
            return 0
        
        # Number string - > int, return within signed 32bit int bounds
        num = int(number_string)
        if num < 0:
            return max(num, umin)
        else:
            return min(num, umax)
