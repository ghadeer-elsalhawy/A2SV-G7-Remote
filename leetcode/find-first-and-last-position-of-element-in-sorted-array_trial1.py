class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # find the first occurance
        left = 0
        right = len(nums) - 1
        begin = float('inf')
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                begin = min(begin, mid)
                right = mid - 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        if begin == float('inf'):
            return [-1, -1]
        # Find last occurance
        left = begin
        right = len(nums) - 1
        end = begin
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                end = max(end, mid)
                left = mid + 1
            else:
                right = mid - 1
        return [begin, end]