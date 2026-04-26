class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        # Is the distance possible
        def ispossible(d):
            counter = 1
            prev = position[0]
            for i in range(len(position)):
                if position[i] - prev >= mid:
                    counter += 1
                    prev = position[i]
                    if counter == m:
                        return True
            return False
        # Binary search
        if m == 2:
            return position[-1] - position[0]
        else:
            res = 0
            left = 0
            right = position[-1] - position[0]
            while left <= right:
                mid = (left + right) // 2
                if ispossible(mid):
                    res = mid
                    left = mid + 1
                else:
                    right = mid - 1
        return res