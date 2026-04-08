class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.nums = []
        self.not_equal = -1

    def consec(self, num: int) -> bool:
        self.nums.append(num)
        # Checking part
        if num != self.value:
            self.not_equal = len(self.nums) - 1

        if len(self.nums) < self.k:
            return False
        
        # len(nums) - 1 --> len(nums) - k - 1

        if len(self.nums) - self.k - 1 < self.not_equal < len(self.nums):
            return False
        return True

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)