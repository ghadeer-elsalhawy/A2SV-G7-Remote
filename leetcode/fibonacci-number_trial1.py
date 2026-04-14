class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        one = 0
        two = 1
        res = 0
        for i in range(2, n + 1):
            res = one + two
            one = two
            two = res
        return res
        