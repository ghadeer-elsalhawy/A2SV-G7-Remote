class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        next_greater = {}
        stack = []
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                next_greater[stack.pop()] = i
            stack.append(i)
        for i in range(len(temperatures)):
            if i not in next_greater:
                next_greater[i] = -1
        
        for i in range(len(temperatures)):
            res[i] = max(0, next_greater[i] - i)
        return res
        