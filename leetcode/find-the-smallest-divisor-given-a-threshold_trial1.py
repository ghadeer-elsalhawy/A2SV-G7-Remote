class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums)
        div = float('inf')
        while left <= right:
            mid = (left + right) // 2
            cur = 0
            for n in nums:
                cur += ceil(n / mid)
            if cur <= threshold:
                div = min(div, mid)
                right = mid - 1
            else:
                left = mid + 1
        return div