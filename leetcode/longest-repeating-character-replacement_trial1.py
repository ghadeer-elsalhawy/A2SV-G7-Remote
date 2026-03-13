class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = Counter(s)
        res = 0
        for dom in freq.keys():
            left = 0
            replace = 0
            for right in range(len(s)):
                if s[right] != dom:
                    while replace >= k:
                        if s[left] != dom:
                            replace -= 1
                        left += 1
                    replace += 1
                res = max(res, right - left + 1)
                # print(s[left:right + 1])
        return res