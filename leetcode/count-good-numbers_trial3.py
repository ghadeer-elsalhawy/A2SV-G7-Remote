class Solution:
    def countGoodNumbers(self, n: int) -> int:
        # There are 4 prime numbers and 5 even for each digit
        res = 0
        mod = 10 ** 9 + 7
        if n&1:
            res = (pow(4, n // 2, mod) * pow(5, n // 2 + 1, mod)) % mod
        else:
            res = (pow(4, n // 2, mod) * pow(5, n // 2, mod)) % mod
        return res