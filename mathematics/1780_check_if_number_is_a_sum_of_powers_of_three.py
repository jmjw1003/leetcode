from collections import deque

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        '''Greedy approach, relies on the fact that 3^i is the largest power of 3 that is less than n'''
        i = 0
        while 3 ** (i + 1) <= n:
            i += 1
        
        while i >= 0:
            power = 3 ** i
            if n - power == 0:
                return True
            if n - power > 0:
                n -= power
            i -= 1
        
        return n == 0

    def checkPowersOfThreeSlower(self, n: int) -> bool:
        '''BFS approach, uses a decision tree to explore all possible sums of powers of 3'''
        decision_tree = deque([0])
        for i in range(16):
            power = 3 ** i
            if power == n:
                return True
            if power > n:
                return False
            for _ in range(len(decision_tree)):
                num = decision_tree.popleft()
                num2 = num + power
                if num2 == n:
                    return True
                decision_tree.extend([num, num2])
        return False