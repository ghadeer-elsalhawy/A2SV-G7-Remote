# Problem Link: https://leetcode.com/problems/two-sum/description/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ind = {}
        for i in range(len(nums)):
            if target - nums[i] in ind:
                return [i, ind[target - nums[i]]]
            ind[nums[i]] = i
          
