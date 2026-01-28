# Problem Link: https://practice.geeksforgeeks.org/problems/check-if-two-arrays-are-equal-or-not3847/1

class Solution:
    def checkEqual(self, a, b) -> bool:
        a.sort()
        b.sort()
        for i in range(len(a)):
            if a[i] != b[i]:
                return False
        return True
