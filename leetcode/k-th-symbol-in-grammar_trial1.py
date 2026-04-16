class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        else:
            order = self.kthGrammar(n - 1, (k + 1) // 2)
            if k&1:
                return order
            else:
                return abs(order - 1)
