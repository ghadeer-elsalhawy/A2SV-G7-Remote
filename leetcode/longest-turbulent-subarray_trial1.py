class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        res = 1
        left = 0
        for right in range(len(arr) - 1):
            if (right % 2 == 0 and arr[right + 1] > arr[right]) or (right&1 and arr[right] > arr[right + 1]):
                res = max(res, right - left + 2)
                
            else:
                left = right + 1
        left = 0
        for right in range(len(arr) - 1):
            if (right % 2 == 0 and arr[right] > arr[right + 1]) or (right&1 and arr[right] < arr[right + 1]):
                res = max(res, right - left + 2)
            else:
                left = right + 1
        return res