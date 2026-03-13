class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        freq = {}
        res = 0
        left = 0
        for right in range(len(fruits)):
            if fruits[right] in freq:
                freq[fruits[right]] += 1
            elif len(freq) < 2:
                freq[fruits[right]] = 1
            else:
                while len(freq) >= 2:
                    freq[fruits[left]] -= 1
                    if freq[fruits[left]] == 0:
                        del freq[fruits[left]]
                    left += 1
                freq[fruits[right]] = 1
            # print(freq)
            res = max(res, sum(freq.values()))
        return res