class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [[1], [1, 1]]
        if rowIndex < len(res):
            return res[rowIndex]
        for i in range(2, rowIndex + 1):
            temp = [1]
            for j in range(len(res[-1]) - 1):
                temp.append(res[-1][j] + res[-1][j + 1])
            temp.append(1)
            res.append(temp)
        return res[rowIndex]