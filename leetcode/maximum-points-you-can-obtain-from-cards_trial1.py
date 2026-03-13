class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        res = 0
        res = sum(cardPoints[:k])
        cur = res
        left = k - 1
        right = len(cardPoints) - 1
        while left >= 0:
            # print(left, right, len(cardPoints))
            cur += cardPoints[right] - cardPoints[left]
            res = max(res, cur)
            left -= 1
            right -= 1
        # print(left, right)
        return res