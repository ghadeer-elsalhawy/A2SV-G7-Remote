class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        maxi = arr[0]
        needop = False
        # print(len(arr))
        if arr[0] == 1:
            for i in range(1, len(arr)):
                if abs(arr[i] - arr[i - 1]) > 1:
                    needop = True
                    break
                else:
                    maxi = max(maxi, arr[i])
        if arr[0] != 1 or needop:
            arr.sort()
            before = 1
            for i in range(1, len(arr)):
                before = min(arr[i], before + 1)
          
            return before

        return maxi
