import math
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        num = ceil(math.log(n, 4))
        if 4 ** num == n:
            return True
        return False