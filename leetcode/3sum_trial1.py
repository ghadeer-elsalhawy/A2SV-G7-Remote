class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] == -nums[i]:
                    res.add((nums[i], nums[left], nums[right]))
                    left += 1
                elif nums[left] + nums[right] < -nums[i]:
                    left += 1
                else:
                    right -= 1
        return list(res)