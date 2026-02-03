Problem Link: https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        result = [0] * len(nums)
        cur_sum = 0
        smaller_than = {}
        for n in sorted(freq):
            smaller_than[n] = cur_sum
            cur_sum += freq[n]
        for i in range(len(nums)):
            result[i] = smaller_than[nums[i]]
        return result
      
