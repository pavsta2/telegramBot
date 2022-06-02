from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        d = deque()
        d.extend(s)
        new_list = []

        while d:

            new_list += [d.popleft()]
            if len(new_list) < 2:
                continue
            if new_list[-2] + new_list[-1] == "()" or new_list[-2] + new_list[-1] == "[]" or new_list[-2] + new_list[-1] == "{}":
                new_list.pop()
                new_list.pop()

        if new_list:
            return False
        else:
            return True

if __name__ == "__main__":
    a = Solution()
    print(a.isValid("()"))
