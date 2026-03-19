class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # the minimum abs diff between target and 3sum
        res = float('inf')
        diff = float('inf')
        nums.sort()
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                temp = nums[i] + nums[left] + nums[right]
                # print(temp)
                if abs(temp - target) < diff:
                    res = temp
                    diff = abs(temp - target)
                if temp >= target:
                    right -= 1
                else:
                    left += 1
        return res