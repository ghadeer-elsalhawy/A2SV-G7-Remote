class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        res = 0
        for left in range(len(word)):
            freq = set()
            for right in range(left, len(word)):
                if word[right] in vowels:
                    freq.add(word[right])
                else:
                    break
                if len(freq) == 5:
                    res += 1
        return res