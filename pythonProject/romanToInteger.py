class Solution:
    def romanToInt(self, s: str) -> int:
        r1 = {"XL": 40, "XC": 90, "CD": 400, "CM": 900, "IV": 4, "IX": 9}
        r2 = {"I": 1, "V": 5, "X": 10, "L":50, "C":100, "D":500, "M":1000}
        integer = 0
        s2 = ""
        while s:
            if s[0:2] in r1.keys():
                integer += r1[s[0:2]]
                s = s.replace(s[0:2], "", 2)
            else:
                s2 += s[0]
                s = s[1:]

        while s2:
            if s2[0:1] in r2.keys():
                integer += r2[s2[0:1]]
                s2 = s2.replace(s2[0:1], "", 1)

        return integer

if __name__ == "__main__":
    a = Solution()
    print(a.romanToInt("MCMXCIV"))

    # s = "CDXLIII"
    # r1 = {"XL": 40, "XC": 90, "CD": 400, "CM": 900, "IV": 4, "IX": 9}
    # r2 = {"I": 1, "V": 5, "X": 10, "L":50, "C":100, "D":500, "M":1000}
    # integer = 0
    # s2 = ""
    # while s:
    #     if s[0:2] in r1.keys():
    #         integer += r1[s[0:2]]
    #         s = s.replace(s[0:2],"",2)
    #     else:
    #         s2 += s[0]
    #         s = s[1:]
    #
    # print(integer)
    # print(s2)
    #
    # while s2:
    #     if s2[0:1] in r2.keys():
    #         integer += r2[s2[0:1]]
    #         s2 = s2.replace(s2[0:1],"",1)
    #
    #
    # print(integer)
    # print(s2)
    #
    # # while s:
    # #     if s[0:2] in r2.keys():
    # #         integer += r1[s[0:2]]
    # #         s = s.strip(s[0:2])
    # #     else:
    # #         s = s.strip(s[0])
    # #
    # # print(integer)
    #
    # # while s:
    # #     for key_ in r1:
    # #         print(s.find(key_),0,2)
    # #         if s.find(key_, 0, 2) == 0:
    # #             integer += r1[key_]
    # #             s = s.strip(key_)
    # #             print(s)
    # # print(integer)
    # # for k2 in r2:
    # #     print(s.find(k2))
    # #     if s.find(k2) > -1:
    # #         integer += r2[k2]
    # #         s = s.replace("key_", "")
    # #         print(s)
    # # print(integer)
    #
    #
