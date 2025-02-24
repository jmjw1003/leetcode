import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        min_speed, max_speed = 1, max(piles)
        k = max_speed
        while min_speed <= max_speed:
            speed = (min_speed + max_speed) // 2
            hours = [math.ceil(pile / speed) for pile in piles]
            if sum(hours) <= h:
                k = min(k, speed)
                max_speed = speed - 1
            else:
                min_speed = speed + 1
        return k
