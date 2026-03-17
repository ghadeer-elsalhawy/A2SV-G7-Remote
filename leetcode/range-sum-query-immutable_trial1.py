class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.res = [0] * (len(self.nums) + 1)
        self.cur = 0
        for i in range(len(self.nums)):
            self.cur += self.nums[i]
            self.res[i + 1] = self.cur

    def sumRange(self, left: int, right: int) -> int:
        return self.res[right + 1] - self.res[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)