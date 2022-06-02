class Solution:
    def climbStairs(self, n: int) -> int:
        climb_ways = [1, 1]
        if n == 1:
            return 1
        elif n == 2:
            return 2

        else:
            for i in range(2, n+1):
                climb_ways.append(climb_ways[i-2] + climb_ways[i - 1])

        return climb_ways[-1]


if __name__ == "__main__":
    a = Solution()
    print(a.climbStairs(2))
