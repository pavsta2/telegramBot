from typing import List


class Solution:
    def searchinsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1

        while True:
            mid = (high + low) // 2
            if nums[mid] == target:
                return mid
            elif low >= high:
                if nums[low] > target:
                    return low
                else:
                    return low + 1
            elif target > nums[mid]:
                low = mid + 1
            elif target < nums[mid]:
                high = mid - 1




if __name__ == "__main__":
    a = Solution()

    print(a.searchinsert([2,3,6,9,11], 1))
