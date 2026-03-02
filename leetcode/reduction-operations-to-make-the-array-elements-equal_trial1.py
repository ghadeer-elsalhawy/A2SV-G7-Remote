class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        counter = 0
        before = nums[0]
        res = 0
        for i, n in enumerate(nums):
            if n > before:
                counter += 1
                before = n
            res += counter
        return res