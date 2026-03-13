class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        res = 0
        odd = []
        for i in range(len(nums)):
            if nums[i]&1:
                odd.append(i)
        if len(odd) < k:
            return 0
        odd.append(len(nums))  
        odd.insert(0, -1)     
        res = 0
        for left in range(1, len(odd) - k):  
            right = left + k - 1
            res += (odd[left] - odd[left-1]) * (odd[right+1] - odd[right])
        return res