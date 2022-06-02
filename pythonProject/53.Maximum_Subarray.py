from typing import List


# class Solution:
def maxsubarray(nums: List[int], left, right) -> int:
    if left == right:
        # if nums[left] > 0:
        return nums[left]
        # else:
        #     return 0

    center = (left + right) // 2
    # Максимальная подпоследовательность левой границы и Максимальная подпоследовательность правой границы
    max_left_sum = maxsubarray(nums, left, center)
    max_right_sum = maxsubarray(nums, center + 1, right)

    max_left_border_sum = left_border_sum = 0
    for i in range(center, left - 1, -1):
        left_border_sum += nums[i]
        if left_border_sum > max_left_border_sum:
            max_left_border_sum = left_border_sum

    max_right_border_sum = right_border_sum = 0
    for i in range(center + 1, right + 1):
        right_border_sum += nums[i]
        if right_border_sum > max_right_border_sum:
            max_right_border_sum = right_border_sum

        # Влево, вправо и подпоследовательности, пересекающие границу
    return max(max_left_sum, max_right_sum, max_left_border_sum + max_right_border_sum)




if __name__ == "__main__":
    print(maxsubarray([-2,1,-3,4,-1,2,1,-5,4],0,8))
