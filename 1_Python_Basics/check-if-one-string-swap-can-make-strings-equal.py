Problem link: https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diff_char_alert = 0
        char_basket = []
        for i in range(len(s1)):
            if s1[i] == s2[i]:
                continue
            else:
                if diff_char_alert >= 2:
                    return False
                if diff_char_alert == 0:
                    char_basket.append(s1[i])
                    char_basket.append(s2[i])
                    diff_char_alert += 1
                else:
                    if s1[i] == char_basket[1] and s2[i] == char_basket[0]:
                        diff_char_alert += 1
                    else:
                        return False
        return diff_char_alert % 2 == 0
