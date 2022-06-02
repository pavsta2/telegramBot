from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        res = 0
        rem = 0

        for i in nums:
            if i == val:
                rem += 1
            else:
                res += 1
        for j in range(rem):
            nums.remove(val)
        nums = nums + [val]*rem
        print(nums)
        return res

if __name__ == "__main__":
    a = Solution()
    print(a.removeElement([3,2,2,3], 3))