class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # so we have to return the starting index of the gas station so that we can come back to tis in  cirular motion
        # brute force would be to loop htorugh gas and cost
        #we try every posible way. we first try the first index and first cost. not possible move on next gastation and cost possible 

        tank = 0
        start = 0

        if sum(gas) < sum(cost):
            return -1

        for i in range(len(gas)):
            tank+= gas[i]-cost[i]

            if tank<0:
                start = i+1
                tank = 0

        return start
            