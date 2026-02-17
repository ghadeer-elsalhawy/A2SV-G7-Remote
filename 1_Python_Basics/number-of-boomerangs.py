# Problem link: https://leetcode.com/problems/number-of-boomerangs/

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        res = 0
        for i in range(len(points)):
            dist_count = defaultdict(int)
            for j in range(len(points)):
                if j == i:
                    continue
                dx = points[i][0] - points[j][0]
                dy = points[i][1] - points[j][1]
                d = dx*dx + dy*dy
                dist_count[d] += 1
            for count in dist_count.values():
                res += count * (count - 1)
        return res
    