class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        left = 0
        res = 1
        double = 0
        for right in range(1, len(s)):
            if s[right] == s[right - 1]:
                while double >= 1:
                    if s[left] == s[left + 1]:
                        double -= 1
                    
                    left += 1
                double += 1
            res = max(res, right - left + 1)
        return res