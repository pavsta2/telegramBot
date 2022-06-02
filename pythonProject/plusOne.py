from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a = 1
        b = -1
        digit = 0
        for i in range(len(digits)):
            digit += digits[b] * a
            a *= 10
            b -= 1
        digit += 1
        answer = []
        for _ in str(digit):
            answer.append(int(_))
        return answer

if __name__ == "__main__":
    a = Solution()
    print(a.plusOne([9]))
    a = [1,2,3,5,6,3,8]
    print(a.)