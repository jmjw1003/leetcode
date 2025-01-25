class Solution:
    def reverse(self, x: int) -> int:
        #TODO: Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

        # 32 bit integer boundaries
        umin, umax = -2 ** 31, (2 ** 31) - 1

        s  = str(x)
        if s[0] == "-":
            s = s[1:]
            num = int("-" + s[::-1])
        else:
            num = int(s[::-1])
        
        if num < umin or num > umax:
            return 0
        
        return num