class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_list = [i.lower() for i in s if i.isalnum()]
        s1 = ''.join(i for i in s_list)
        s_list.reverse()
        s2 = ''.join(i for i in s_list)
        if s1 == s2:
            return True
        else:
            return False


if __name__ == "__main__":
    x = Solution()
    print(x.isPalindrome("race a car"))