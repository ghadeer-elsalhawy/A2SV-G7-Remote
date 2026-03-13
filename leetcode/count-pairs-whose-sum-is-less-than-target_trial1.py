class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        print(nums)
        res = 0
        barrier = len(nums)
        for left in range(len(nums)):
            for right in range(left + 1, barrier):
                if nums[left] + nums[right] < target:
                    res += 1
                else:
                    barrier = right
                    break
        return res
        