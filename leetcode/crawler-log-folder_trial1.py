class Solution:
    def minOperations(self, logs: List[str]) -> int:
        level = 0
        for d in logs:
            if d == "../":
                level = max(0, level - 1)
            elif d == "./":
                continue
            else:
                level += 1
        return level