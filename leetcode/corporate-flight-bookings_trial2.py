class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0] * (n + 1)
        tot = [0] * n
        for s, e, b in bookings:
            res[s - 1] += b
            res[e] -= b
        cur = 0
        for i in range(n):
            cur += res[i]
            tot[i] += cur
        return tot