# Problem Lin: https://leetcode.com/problems/majority-element-ii/

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        res = []
        for k, v in freq.items():
            if v > len(nums) / 3:
                res.append(k)
        return res
