from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if len(strs) == 1:
            return strs[0]

        ind = 0
        prefix_final = ""
        while True:
            result = 0
            prefix = strs[0][ind]
            for i in strs:
                if ind <= (len(i)-1) and prefix == i[ind]:
                    result += 1
            if result == len(strs):
                prefix_final += prefix
                ind += 1
                if ind >= (len(strs[0])):
                    return prefix_final
            else:
                return prefix_final

if __name__ == "__main__":
    a = Solution()
    print(a.longestCommonPrefix(["flower","flower","flower","flower"]))
