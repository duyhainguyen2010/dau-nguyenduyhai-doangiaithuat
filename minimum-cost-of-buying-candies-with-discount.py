class Solution(object):
    def minimumCost(self, cost):
        cost.sort()
        result = 0
        count = 0
        for i in range(len(cost) - 1, -1, -1):
            count += 1
            if count % 3 != 0:
                result += cost[i]

        return result
