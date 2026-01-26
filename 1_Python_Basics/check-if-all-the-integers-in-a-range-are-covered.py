# Problem Link: https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        covered = [0] * 52
        for begin, end in ranges:
            covered[begin] += 1
            covered[end + 1] -= 1
        print(covered)
        # check if left bound is covered
        cur = 0
        for i in range(left + 1):
            cur += covered[i]
        if cur <= 0:
            return False
        for pointer in range(left + 1, right + 1):
            cur += covered[pointer]
            if cur <= 0:
                return False
        return True
