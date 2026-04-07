class Solution:
    def isValid(self, s: str) -> bool:
        valid = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for l in s:
            if l in valid:
                stack.append(l)
            else:
                if not stack: return False
                last = stack.pop()
                if valid[last] != l:
                    return False
        return not stack