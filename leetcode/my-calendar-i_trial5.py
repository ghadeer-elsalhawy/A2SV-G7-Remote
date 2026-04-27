class MyCalendar:

    def __init__(self):
        self.times = []

    def book(self, startTime: int, endTime: int) -> bool:
        self.times.sort()
        left = 0
        right = len(self.times) - 1
        while self.times and left <= right:
            mid = (left + right) // 2
            if self.times[mid][0] <= startTime < self.times[mid][1] or self.times[mid][0] < endTime < self.times[mid][1] or startTime <= self.times[mid][0] < endTime or startTime < self.times[mid][1] < endTime:
                return False
            elif startTime >= self.times[mid][1]:
                left = mid + 1
            else:
                right = mid - 1
        self.times.append([startTime, endTime])
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)