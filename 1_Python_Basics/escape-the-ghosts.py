# Problem link: https://leetcode.com/problems/escape-the-ghosts/

class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        min_ghost_dist = float('inf')
        for g in ghosts:
            min_ghost_dist = min(min_ghost_dist, abs(g[0] - target[0]) + abs(g[1] - target[1]))
        self_dist = abs(target[0]) + abs(target[1])
        if min_ghost_dist <= self_dist:
            return False
        return True
    