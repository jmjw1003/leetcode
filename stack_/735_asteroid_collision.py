class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []
        for asteroid in asteroids:
            if asteroid > 0:
                stack.append(asteroid)
            else:
                right = abs(asteroid)
                if not stack or stack[-1] < 0:
                    stack.append(asteroid)
                else:
                    while stack and right and not stack[-1] < 0:
                        if stack[-1] == right:
                            stack.pop()
                            right = None
                        elif stack[-1] > right:
                            right = None
                        else:
                            stack.pop()
                    if right:
                        stack.append(asteroid)
        return stack
    

# x = Solution().asteroidCollision([5,-2,-1,1,2])
x = Solution().asteroidCollision([-2,-2,1,-2])
print(x)