class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ordered = sorted(score, reverse=True)
        rank = {}
        for i, o in enumerate(ordered):
            rank[o] = i
        res = []
        for s in score:
            if rank[s] > 2:
                res.append(str(rank[s] + 1))
            else:
                if rank[s] == 0:
                    res.append("Gold Medal")
                elif rank[s] == 1:
                    res.append("Silver Medal")
                else:
                    res.append("Bronze Medal")
        return res