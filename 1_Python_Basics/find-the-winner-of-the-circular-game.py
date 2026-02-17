# Problem link: https://leetcode.com/problems/find-the-winner-of-the-circular-game/description/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        q = [i for i in range(1, n + 1)]
        p = 0
        while len(q) != 1:
            to_remove = (p + k - 1) % len(q)
            q.pop(to_remove)
            p = to_remove
            if p >= len(q):
                p = 0
        return q[0]
    