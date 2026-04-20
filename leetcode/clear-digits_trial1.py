class Solution:
    def clearDigits(self, s: str) -> str:
        res = []
        for l in s:
            if l.isdigit():
                if res:
                    res.pop()
            else:
                res.append(l)
        return "".join(res)