class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        s = 0
        freq = set()
        left = 0
        for right in range(len(nums)):
            if nums[right] not in freq:
                s += nums[right]
                freq.add(nums[right])
            else:
                while nums[left] != nums[right]:
                    s -= nums[left]
                    freq.remove(nums[left])
                    left += 1
                left += 1
            while right - left + 1 > k:
                s -= nums[left]
                freq.remove(nums[left])
                left += 1
            if right - left + 1 == k:
                res = max(res, s)               
        return res