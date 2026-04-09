class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1] * len(nums)
        stack = []      # strictly decreasing
        for i, n in enumerate(nums):
            while stack and nums[stack[-1]] < n:
                res[stack.pop()] = n
            stack.append(i)
        print(stack)
        for i, n in enumerate(nums):
            while stack and nums[stack[-1]] < n:
                if res[stack[-1]] == -1:
                    res[stack.pop()] = n
                else:
                    stack.pop()
            stack.append(i)

        return res