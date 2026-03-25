class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        rem = {0: -1}
        cur = 0
        for i, n in enumerate(nums):
            cur += n
            if cur % k in rem:
                if i - rem[cur % k] >= 2:
                    return True
            else:
                rem[cur % k] = i
        return False