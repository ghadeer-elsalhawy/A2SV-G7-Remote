class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        res = 0
        x = [p[0] for p in points]
        x.sort()
        for i in range(len(x) - 1):
            res = max(res, x[i + 1] - x[i])
        return res