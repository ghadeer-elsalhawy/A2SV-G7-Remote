# Problem link: https://leetcode.com/problems/sum-in-a-matrix/

class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        res = 0
        rounds = len(nums[0])

        for _ in range(rounds):
            max_list = []
            for i in range(len(nums)):
                maxi = -1
                idx = set()
                for j in range(len(nums[0])):
                    if maxi < nums[i][j]:
                        maxi = nums[i][j]
                        idx = (i, j)
                max_list.append((maxi, idx))
            max_list.sort()
            res += max_list[-1][0]
            for (val, idx) in max_list:
                nums[idx[0]][idx[1]] = -1
        return res
    