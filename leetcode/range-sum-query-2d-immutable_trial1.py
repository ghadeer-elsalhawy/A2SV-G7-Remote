class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.mat = matrix
        self.m = len(matrix[0])
        self.n = len(matrix)
        self.pre = [[0] * (self.m + 1) for _ in range(self.n + 1)]
        for i in range(self.n):
            for j in range(self.m):
                self.pre[i + 1][j + 1] = self.mat[i][j] + self.pre[i][j + 1] + self.pre[i + 1][j] - self.pre[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (self.pre[row2 + 1][col2 + 1] - self.pre[row1][col2 + 1] 
                - self.pre[row2 + 1][col1] + self.pre[row1][col1])


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)