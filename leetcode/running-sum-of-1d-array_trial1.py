class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        cur = 0
        res = [0] * len(nums)
        for i in range(len(nums)):
            cur += nums[i]
            res[i] = cur
        return res
