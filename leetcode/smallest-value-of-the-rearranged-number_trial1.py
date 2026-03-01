class Solution:
    def smallestNumber(self, num: int) -> int:
        res = 0
        if num > 0:
            s = [n for n in str(num)]
            s.sort()
            print(s)
            i = -1
            while s[i + 1] == "0":
                i += 1
            print("zeros", i)
            if i == -1:
                res = "".join(s)
            else:
                temp = [s[i + 1]] + ["0"] * (i + 1) + s[i + 2:]
                print(temp)
                res = "".join(temp)
                # print(res)

        elif num < 0:
            s = sorted([n for n in str(abs(num))], reverse=True)
            res = - int("".join(s))
        return int(res)
