from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums_set = sorted(list(set(nums)))
        k = 0
        for i in range(0, len(nums_set)):
            nums[i] = nums_set[i]
            k += 1

        return k



if __name__ == "__main__":
    c = Solution()
    print(c.removeDuplicates([-1,0,0,0,0,3,3]))
