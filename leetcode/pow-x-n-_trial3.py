class Solution:
    def myPow(self, x: float, n: int) -> float:
        def calc(x, n):
            if n == 0:
                return 1
            half = calc(x, n // 2)
            return x * half * half if n & 1 else half * half
                
        tot = calc(x, abs(n))
        if n >= 0:
            return tot
        else:
            return 1 / tot