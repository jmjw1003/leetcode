class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        # Check there is a possible solution
        if sum(gas) < sum(cost):
            return -1
        
        start = 0
        total = 0
        for i in range(len(gas)):
            gas_diff = gas[i] - cost[i]
            total += gas_diff
            if total < 0:
                total = 0
                start = i + 1

        return start