class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur = sum(nums[:k])
        res = cur
        for i in range(k, len(nums)):
            cur -= nums[i - k]
            cur += nums[i]
            res = max(res, cur)
        return res / k