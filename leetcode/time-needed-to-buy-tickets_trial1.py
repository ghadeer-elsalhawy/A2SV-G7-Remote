class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        res = tickets[k]
        for i in range(k):
            res += min(tickets[i], tickets[k])
        for i in range(k + 1, len(tickets)):
            res += min(tickets[i], tickets[k] - 1)
        return res