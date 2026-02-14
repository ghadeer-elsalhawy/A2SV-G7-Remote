# Problem link: https://leetcode.com/problems/keyboard-row/submissions/1918252713/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        def checkLine(w, key):
            for l in w:
                if l.lower() not in key:
                    return False
            return True
        l1 = "qwertyuiop"
        l2 = "asdfghjkl"
        l3 = "zxcvbnm"
        res = []
        for w in words:
            check = False
            if w[0].lower() in l1:
                check = checkLine(w, l1)
            elif w[0].lower() in l2:
                check = checkLine(w, l2)
            else:
                check = checkLine(w, l3)
            if check:
                res.append(w)
        return res
    