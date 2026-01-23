# Problem Link: https://leetcode.com/problems/find-players-with-zero-or-one-losses/description/

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        final = defaultdict(int)
        players = set()
        for winner, loser in matches:
            players.add(winner)
            players.add(loser)
            final[loser] += 1
        zero, one = [], []
        for p in players:
            if p not in final:
                zero.append(p)
            elif final[p] == 1:
                one.append(p)
        return [sorted(zero), sorted(one)]
