# Problem link: https://leetcode.com/problems/flipping-an-image/description/

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        res = []
        for r in image:
            res.append(r[::][::-1])
        for r in range(len(image)):
            for c in range(len(image[0])):
                res[r][c] ^= 1
        return res
