class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = weights[0]
        right = sum(weights)
        res = float('inf')
        while left <= right:
            cap = left + (right - left) // 2
            total = 0
            rem = cap
            for i in range(len(weights)):
                if weights[i] > cap:
                    total = float('inf')
                    break
                if weights[i] <= rem:
                    rem -= weights[i]
                else:
                    total += 1
                    rem = cap - weights[i]
            if rem != cap:
                total += 1
            if total <= days:
                res = min(res, cap)
                right = cap - 1
            else:
                left = cap + 1
        return res