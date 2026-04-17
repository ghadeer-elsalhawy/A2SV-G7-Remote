class Solution:
    def decodeString(self, s: str) -> str:
        count_stack = []
        string_stack = []
        current = ""
        k = 0

        for char in s:
            if char.isdigit():
                k = k * 10 + int(char)
            
            elif char == "[":
                count_stack.append(k)
                string_stack.append(current)
                current = ""
                k = 0
            
            elif char == "]":
                repeat = count_stack.pop()
                prev = string_stack.pop()
                current = prev + current * repeat
            else:
                current += char
        return current