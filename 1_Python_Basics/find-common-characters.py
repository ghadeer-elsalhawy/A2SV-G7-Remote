Problem link: https://leetcode.com/problems/find-common-characters/

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        freq = Counter(words[0])
        for w in words:
            d = Counter(w)
            for k in freq.keys():
                freq[k] = min(freq[k], d[k])
        res = []
        for k, v in freq.items():
            for i in range(1, v + 1):
                res.append(k)
        return res
      
