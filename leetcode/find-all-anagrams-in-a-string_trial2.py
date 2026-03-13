class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        k = len(p)
        comp = sorted(p)
        for i in range(len(s) - k + 1):
            # print(s[i: i + k], p)
            if sorted(s[i: i + k]) == comp:
                res.append(i)
        return res