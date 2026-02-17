# Problem link: https://leetcode.com/problems/unique-morse-code-words/

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        tran = defaultdict(int)
        for w in words:
            code = ""
            for l in w:
                code += morse[ord(l) - 97]
            tran[code] += 1
        return len(tran)
    