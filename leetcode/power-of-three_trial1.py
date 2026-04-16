class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        temp = ceil(math.log(n, 3))
        if 3 ** temp == n:
            return True
        return False