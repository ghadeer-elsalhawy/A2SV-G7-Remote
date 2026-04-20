class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            if a > 0:
                stack.append(a)
            else:
                explode = False
                while stack and not explode:
                    if stack[-1] < 0:
                        break
                    else:
                        if stack[-1] < abs(a):
                            stack.pop()
                        elif stack[-1] == abs(a):
                            explode = True
                            stack.pop()
                        else:
                            explode = True
                if not explode:
                    stack.append(a)
        return stack