class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        # Find rotation point
        if nums[-1] < nums[0]:
            left, right = 0, len(nums) - 1
            while left < right:
                mid = (left + right) // 2
                if nums[mid] > nums[right]:
                    left = mid + 1 
                else:
                    right = mid    
            start = left   
        # Find which half to search in      
        if target > nums[-1]:
            left = 0
            right = start - 1
        else:
            left = start
            right = len(nums) - 1
        # Find target in the array
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1