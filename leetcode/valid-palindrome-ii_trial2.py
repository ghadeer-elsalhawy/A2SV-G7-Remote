class Solution:
    def validPalindrome(self, s: str) -> bool:
        def checkwithdelete(l, r):
            print(l, r)
            while l < r < len(s):
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1

            else:
                if not checkwithdelete(left, right - 1) and not checkwithdelete(left + 1, right):
                    return False
                break 
        return True