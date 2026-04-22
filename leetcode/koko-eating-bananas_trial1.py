class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = sum(piles)
        res = float('inf')
        while left <= right:
            cur = 0
            mid = (left + right) // 2
            for b in piles:
                cur += ceil(b / mid)
                # print(cur)
            if cur <= h:
                res = min(res, mid)
                right = mid - 1
            else:
                left = mid + 1
        return res