# Problem link: https://leetcode.com/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left, right = 0, len(matrix[0])
        up, down = 0, len(matrix)
        while left <= right and up <= down:
            res += matrix[up][left: right]
            up += 1
            
        return res
    