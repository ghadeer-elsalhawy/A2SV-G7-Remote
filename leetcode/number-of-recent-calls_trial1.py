class RecentCounter:

    def __init__(self):
        self.r = deque()
        

    def ping(self, t: int) -> int:
        self.r.append(t)
        while self.r[0] < t - 3000:
            self.r.popleft()
        return len(self.r)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)