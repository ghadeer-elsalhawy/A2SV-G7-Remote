class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        point = 0
        while point < n:
            if arr[point] == 0:
                arr.insert(point, 0)
                point += 2
                arr.pop(-1)
            else:
                point += 1
            # print(arr)
        