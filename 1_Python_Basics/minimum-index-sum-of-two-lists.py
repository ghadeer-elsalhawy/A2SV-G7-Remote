# Problem link: https://leetcode.com/problems/minimum-index-sum-of-two-lists/

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        freq = {}
        for i, w in enumerate(list1):
            freq[w] = [i]
        min_idx = float('inf')
        for i, w in enumerate(list2):
            if w in freq:
                freq[w].append(i)
                min_idx = min(min_idx, sum(freq[w]))
        
        res = []
        for k, v in freq.items():
            if len(v) == 2 and sum(v) == min_idx:
                res.append(k)
        return res
