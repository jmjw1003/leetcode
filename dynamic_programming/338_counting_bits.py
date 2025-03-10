class Solution:
    def countBits(self, n: int) -> list[int]:
        bit_count = [0] * (n + 1)
        offset = 1 # keep track of highest power of 2
        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            bit_count[i] = 1 + bit_count[i - offset]
        return bit_count
