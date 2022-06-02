class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                a = nums[i] + nums[j]

                if a == target:
                    return [i,j]


if __name__ == "__main__":
    a = Solution()
    print(a.twoSum([2,7,11,15], 9))
