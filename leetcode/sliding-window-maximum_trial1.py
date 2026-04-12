class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = [-1] * (len(nums) - k + 1)
        left = 0
        stack = deque()  # decreasing
        for right in range(len(nums)):
            while stack and stack[-1] < nums[right]:
                stack.pop()
            stack.append(nums[right])
            while right - left + 1 > k:
                if nums[left] == stack[0]:
                    stack.popleft()
                left += 1
            if right - left + 1 == k:
                res[left] = stack[0]
        return res