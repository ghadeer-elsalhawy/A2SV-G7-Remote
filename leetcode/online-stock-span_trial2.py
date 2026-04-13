class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        max_days = 1
        while self.stack and self.stack[-1][0] <= price:
            max_days += self.stack.pop()[1]
        self.stack.append((price, max_days))
        return max_days


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)