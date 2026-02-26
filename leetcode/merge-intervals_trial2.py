class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        left, right = intervals[0][0], intervals[0][1]
        for start, end in intervals:
            if start > right:
                res.append([left, right])
                left = start
                right = end
            else:
                right = max(right, end)
        res.append([left, right])
        return res