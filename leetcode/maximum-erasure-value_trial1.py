class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        res = 0
        visited = set()
        left = 0
        cur = 0
        for right in range(len(nums)):
            while nums[right] in visited:
                visited.remove(nums[left])
                cur -= nums[left]
                left += 1
            visited.add(nums[right])
            cur += nums[right]
            res = max(res, cur)
        return res