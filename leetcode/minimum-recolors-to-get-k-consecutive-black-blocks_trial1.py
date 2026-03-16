class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = 0
        recolor = 0
        res = k
        for right in range(len(blocks)):
            if blocks[right] == 'W':
                recolor += 1
            while right - left + 1 > k:
                if blocks[left] == 'W':
                    recolor -= 1
                left += 1
            if right - left + 1 == k:
                res = min(res, recolor)
        return res
        