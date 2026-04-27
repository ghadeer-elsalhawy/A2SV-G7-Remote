class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        maxi = 0
        cur = 1
        left = 0
        for right in range(len(nums)):
            cur *= nums[right]
            while cur >= k and left <= right:
                cur //= nums[left]
                left += 1
            maxi += (right - left + 1)
        return maxi 