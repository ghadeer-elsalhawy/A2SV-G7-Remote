class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        res = [-1] * len(nums)
        n = 2 * k + 1
        counter = 0
        left = 0
        cur = 0
        for right in range(len(nums)):
            cur += nums[right]
            counter += 1
            while counter > n:
                counter -= 1
                cur -= nums[left]
                left += 1
            if counter == n:
                print(cur)
                res[right - k] = cur // n
        return res