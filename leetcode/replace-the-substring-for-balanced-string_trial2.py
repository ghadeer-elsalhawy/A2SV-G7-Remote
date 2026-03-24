class Solution:
    def balancedString(self, s: str) -> int:
        target = len(s) // 4
        freq = Counter(s) 
        
        if all(freq[c] == target for c in "QWER"):
            return 0
        
        res = len(s)
        left = 0
        
        for right in range(len(s)):
            freq[s[right]] -= 1 
            
            while left <= right and all(freq[c] <= target for c in "QWER"):
                res = min(res, right - left + 1)
                freq[s[left]] += 1  
                left += 1
        
        return res