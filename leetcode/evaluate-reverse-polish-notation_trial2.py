class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            # print(stack)
            if t not in ["+", "-", "*", "/"]:
                stack.append(int(t))
            else:
                one = int(stack.pop())
                two = int(stack.pop())
                res = 0
                if t == "-":
                    res = two - one
                elif t == "+":
                    res = one + two
                elif t == "*":
                    res = one * two
                else:
                    res = int(two / one)
                stack.append(res)
    
        return stack[0]