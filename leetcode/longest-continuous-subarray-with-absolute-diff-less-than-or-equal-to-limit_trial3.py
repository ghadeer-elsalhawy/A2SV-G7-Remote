class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        res = 1
        maxi_stack = deque()    # Holding minimum value at index 0
        mini_stack = deque()    # Holding maximum value at index 0
        left = 0
        for right in range(len(nums)):
            while maxi_stack and maxi_stack[-1] > nums[right]:
                maxi_stack.pop()
            maxi_stack.append(nums[right])
            while mini_stack and mini_stack[-1] < nums[right]:
                mini_stack.pop()
            mini_stack.append(nums[right])
            while mini_stack[0] - maxi_stack[0] > limit:
                if nums[left] == maxi_stack[0]:
                    maxi_stack.popleft()
                if nums[left] == mini_stack[0]:
                    mini_stack.popleft()
                left += 1
            res = max(res, right - left + 1)
        return res