class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        step = 0
        before = nums[0]
        for n in nums:
            if n > before:
                step += 1
                before = n
            res += step
        return res