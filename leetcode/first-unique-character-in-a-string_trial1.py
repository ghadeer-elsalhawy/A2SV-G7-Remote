class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = Counter(s)
        for i, l in enumerate(s):
            if freq[l] == 1:
                return i
        return -1