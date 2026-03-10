class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2: return len(s)
        res = 1
        left = 0
        cur = 1
        for right in range(1, len(s)):
            while s[right] in s[left:right]:
                left += 1
                cur -= 1 
            cur += 1
            # print(s[left: right + 1])
            res = max(res, cur)
        return res