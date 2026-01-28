# Problem Link: https://practice.geeksforgeeks.org/problems/union-of-two-arrays3538/1

class Solution:    
    def findUnion(self, a, b):
        # code here
        result = set(a + b)
        return list(result)
