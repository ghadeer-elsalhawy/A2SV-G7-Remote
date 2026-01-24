# Problem Link: https://leetcode.com/problems/majority-element/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = Counter(nums)
        for k, v in freq.items():
            if v > len(nums) / 2:
                return k
