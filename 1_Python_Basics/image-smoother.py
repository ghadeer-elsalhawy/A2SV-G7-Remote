# Problem link: https://leetcode.com/problems/image-smoother/

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        res = [[0 for _ in range(len(img[0]))] for j in range(len(img))]
        for row in range(len(img)):
            for col in range(len(img[0])):
                counter = 0
                total = 0
                for i in range(row - 1, row + 2):
                    for j in range(col - 1, col + 2):
                        if i >= 0 and i < len(img) and j >= 0 and j < len(img[0]):
                            counter += 1
                            total += img[i][j]
                res[row][col] = floor(total / counter)     
        return res