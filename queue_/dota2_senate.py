from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        length = len(senate)
        direQueue, radiantQueue = deque(), deque()
        for i in range(length):
            if senate[i] == "R":
                radiantQueue.append(i)
            else:
                direQueue.append(i)

        while radiantQueue and direQueue:
            radiantSenator = radiantQueue.popleft()
            direSenator = direQueue.popleft()

            if radiantSenator < direSenator:
                radiantQueue.append(radiantSenator + length)
            else:
                direQueue.append(direSenator + length)
            
        return "Radiant" if radiantQueue else "Dire"


solution = Solution()

sen1 = ["R", "D"]
sen2 = ["D", "D", "D", "R", "R", "R", "R"]

print(sen1, solution.predictPartyVictory(sen1))
print(sen2, solution.predictPartyVictory(sen2))