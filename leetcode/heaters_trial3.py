class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        left = 0
        right = 10**9
        res = float('inf')
        while left <= right:
            p = 0 
            mid = (left + right) // 2
            stat = True
            for i in range(len(houses)):
                while p < len(heaters) and heaters[p] + mid < houses[i]:
                    p += 1
                if p == len(heaters) or heaters[p] - mid > houses[i]:
                    stat = False
                    break
        
            if stat:
                res = min(res, mid)
                right = mid - 1
            else: 
                left = mid + 1 
        return res