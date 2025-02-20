class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []
        
        for asteroid in asteroids:
            if not stack:
                stack.append(asteroid)
            # R + R, or L + any direction
            elif (stack[-1] > 0 and asteroid > 0) or (stack[-1] < 0):
                stack.append(asteroid)
            # R + L -> clash
            else:
                # Round 1, FIGHT!
                while stack and stack[-1] > 0:
                    if stack[-1] == abs(asteroid):
                        stack.pop()
                        break
                    elif stack[-1] < abs(asteroid):
                        stack.pop()
                        if not stack or stack[-1] < 0:
                            stack.append(asteroid)
                            break
                    else:
                        break
        return stack
