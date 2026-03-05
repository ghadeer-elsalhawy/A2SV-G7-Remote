class Solution:
    def frequencySort(self, s: str) -> str:
        freq = defaultdict(int)
        for l in s:
            freq[l] += 1
        res = ""
        ss = sorted(freq.items(), key=lambda x:x[1], reverse=True)
        for k, v in ss:
            res += k * v
        return res