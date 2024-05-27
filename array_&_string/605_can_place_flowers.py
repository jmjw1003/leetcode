class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True

        l = len(flowerbed)
        to_plant = n

        for i in range(l):

            if i == 0:
                if not sum(flowerbed[i : i + 2]):
                    flowerbed[i] = 1
                    to_plant -= 1
                    if to_plant == 0:
                        return True
            
            else:
                if sum(flowerbed[i - 1: i + 2]) == 0:
                    flowerbed[i] = 1
                    to_plant -= 1
                    if to_plant == 0:
                        return True
            
        return False