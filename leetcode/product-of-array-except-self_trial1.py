class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1] * len(nums)
        post = [1] * len(nums)
        cur = 1
        for i in range(1, len(nums)):
            cur *= nums[i - 1]
            pre[i] = cur
        cur = 1
        for i in range(len(nums) - 2, -1, -1):
            cur *= nums[i + 1]
            post[i] = cur
        res = [0] * len(nums)
        for i in range(len(nums)):
            res[i] = pre[i] * post[i]
        return res