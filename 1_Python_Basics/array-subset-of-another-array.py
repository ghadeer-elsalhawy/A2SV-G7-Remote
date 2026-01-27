# Problem Link: https://practice.geeksforgeeks.org/problems/array-subset-of-another-array2317/1

from collections import Counter
class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        freq = Counter(a)
        for element in b:
            if element not in freq or freq[element] <= 0:
                return False
            else:
                freq[element] -= 1
        return True
    
