Problem link: https://leetcode.com/problems/final-value-of-variable-after-performing-operations/description/

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        # First approach
        # res = 0
        # for op in operations:
        #     if op == "++X" or op == "X++":
        #         res += 1
        #     else:
        #         res -= 1
        # return res
        ##########
        # Second approach
        freq = Counter(operations)
        res = freq["X++"] + freq["++X"] - freq["X--"] - freq["--X"]
        return res
