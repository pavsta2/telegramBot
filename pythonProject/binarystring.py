import re
from re import sub

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c_int = int(a) + int(b)
        c_list = [int(i) for i in list(str(c_int))]

        for i in range(-1,-(len(c_list)),-1):
            if c_list[i] == 2:
                c_list[i] = 0
                c_list[i-1] += 1
            elif c_list[i] == 3:
                c_list[i] = 1
                c_list[i - 1] += 1
        if c_list[0] == 2:
            c_list[0] = 10
        if c_list[0] == 3:
            c_list[0] = 11

        c_str = str(c_list)
        result = ''.join(i for i in c_str if i.isdigit())

        # c_str = str(c_list)
        # c_str = c_str.replace('[', '')
        # c_str = c_str.replace(']', '')
        # c_str = c_str.replace(', ', '')

        return result

if __name__ == "__main__":
    a = Solution()
    print(a.addBinary('1111','1111'))
