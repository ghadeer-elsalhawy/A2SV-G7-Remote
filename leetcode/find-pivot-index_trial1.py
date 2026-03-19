class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        cur = 0
        pre = [0] * len(nums)
        for i in range(1, len(nums)):
            cur += nums[i - 1]
            pre[i] = cur
        cur = 0
        post = [0] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            cur += nums[i + 1]
            post[i] = cur
        # print(pre)
        # print(post)
        for i in range(len(nums)):
            if pre[i] == post[i]:
                return i 
        return -1