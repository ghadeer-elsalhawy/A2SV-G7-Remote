class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        res = 0
        left = 0
        cur = 0
        for right in range(len(s)):
            if s[right] in vowels:
                cur += 1
            while right - left + 1 > k:
                if s[left] in vowels:
                    cur -= 1
                left += 1
            if right - left + 1 == k:
                res = max(res, cur)
        return res