# Problem link: https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        pointer = 0
        temp = str(x)
        for pointer in range(len(temp) // 2 + 1):
            if temp[pointer] != temp[len(temp) - 1 - pointer]:
                return False
        return True
