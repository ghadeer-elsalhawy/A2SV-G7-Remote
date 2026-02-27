class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq = Counter(nums)
        color = 0
        for i in range(len(nums)):
            while color not in freq or freq[color] == 0:
                color += 1
            nums[i] = color
            freq[color] -= 1