class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        turn = [0] * (len(s) + 1)

        for st, e, d in shifts:
            move = 0
            if d == 1:
                move = 1
            else:
                move = -1
            turn[st] += move
            turn[e + 1] -= move
        
        res = ""
        cur = 0
        for i in range(len(s)):
            cur += turn[i]
            print(chr((ord(s[i]) - ord('a') + cur) % 26 + ord('a')))
            res += chr(((ord(s[i]) - ord('a') + cur) % 26) + ord('a'))
        return res