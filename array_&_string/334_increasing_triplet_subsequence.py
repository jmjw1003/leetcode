class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        """
        Keep track of increasing pair (vars first, second).
        
        Go through nums in order.

        If we reach the condition that second has been "filled",
        then any greater following number fulfils the condition.

        Aim is to keep second number in the increasing pair as small
        as possible.
        """
        first, second = float("inf"), float("inf")

        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
    
        return False
