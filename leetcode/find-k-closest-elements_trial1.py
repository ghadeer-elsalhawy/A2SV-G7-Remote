class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        close = []
        place = -1
        # find the middle point
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] <= x:
                place = mid
                left = mid + 1
            else:
                right = mid - 1
        # Find the array
        if place == -1 and x > arr[-1]: # Bigger than all number start from end
            return arr[-k:]
        elif place == -1 and x < arr [0]: # Smaller than all numbers start from beginning
            return arr[:k]
        else:  # Lying in the middle
            before = place
            after = place + 1
            while k > 0:
                if after >= len(arr) or abs(arr[before] - x) <= abs(arr[after] - x):
                    before -= 1
                else:
                    after += 1
                k -= 1
            return arr[before + 1: after]