class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = heights[0]
        stack = []
        heights.append(-1)
        for i, h in enumerate(heights):
            while (stack and heights[stack[-1]] > h):
                local_max = heights[stack.pop()]
                if not stack:
                    width = i
                else:
                    width = i - stack[-1] - 1
                res = max(res, width * local_max)
            stack.append(i)

        return res