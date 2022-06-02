from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        total_costs = [float("+inf")] * len(cost)
        total_costs[0] = cost[0]
        total_costs[1] = cost[1]

        for i in range(len(cost)-2):
            total_costs[i+2] = min(total_costs[i]+cost[i+2], total_costs[i+1]+cost[i+2])
        #     total_costs[i] = min(
        #         total_costs[i-2] + cost[i],
        #         total_costs[i-1] + cost[i])
        result = min(total_costs[-1], total_costs[-2])

        return result

if __name__ == "__main__":
    a = Solution()
    print(a.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))