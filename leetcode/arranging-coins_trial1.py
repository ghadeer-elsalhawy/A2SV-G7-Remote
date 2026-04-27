class Solution:
    def arrangeCoins(self, n: int) -> int:
        res = 0
        left = 1
        right = n
        while left <= right:
            mid = (left + right) // 2 
            if ((mid + 1) * mid) // 2 <= n:
                res = max(res, mid)
                left = mid + 1
            else:
                right = mid - 1
        return res