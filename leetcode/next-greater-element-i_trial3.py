class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        stack = [] 
        res = [-1] * len(nums1)
        dic = {}
        for n in nums2:
            while stack and stack[-1] < n:
                dic[stack.pop()] = n
            stack.append(n)

        for i in stack:
            dic[i] = -1

        for i, n in enumerate(nums1):
            res[i] = dic[n]
        return res