from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not nums1 or not nums2:
            nums1.extend(nums2)
        if n == 0:
            return nums1
        if m == 0:
            nums1.clear()
            for i in nums2:
                nums1.append(i)
        for i in range(n):
            nums1[m] = nums2[i]
            m += 1
        nums1.sort()
        return nums1

if __name__ == "__main__":
    a = Solution()
    print(a.merge([0], 0, [1], 1))
