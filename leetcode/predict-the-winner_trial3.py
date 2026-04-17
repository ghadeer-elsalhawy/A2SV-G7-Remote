class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def findmaxi(left, right):
            if left > right: # Base case
                return 0
            return max(nums[left] - findmaxi(left + 1, right), nums[right] - findmaxi(left, right - 1))
        dist = findmaxi(0, len(nums) - 1)
        if dist >= 0:
            return True
        return False