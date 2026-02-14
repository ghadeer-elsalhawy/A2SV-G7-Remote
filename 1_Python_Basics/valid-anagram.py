# Problem Link: https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1 = [l for l in s]
        l2 = [l for l in t]
        return sorted(l1) == sorted(l2)