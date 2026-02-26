class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        point = len(arr) - 1
        while point > 0:
            maxi = arr[0]
            idx = 0
            for i in range(point + 1):
                if arr[i] > maxi:
                    maxi = arr[i]
                    idx = i
            if idx != point:
                print(idx)
                print("Before", arr)
                arr = arr[:idx + 1][::-1] + arr[idx + 1:]
                print("Middle", arr)
                arr = arr[:point + 1][::-1] + arr[point + 1:]
                print("Last", arr)
                res.append(idx + 1)
                res.append(point + 1)
            point -= 1
        return res