class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def check(idx_s, idx_p):
            if idx_p == len(p):
                if idx_s == len(s):
                    return True
                else:
                    return False
            if idx_s == len(s):
                for i in range(idx_p, len(p), 2):
                    if i + 1 < len(p) and p[i + 1] == "*":
                        continue
                    else:
                        return False 
                return True   
            if idx_p + 1 < len(p) and p[idx_p + 1] == '*':
                current_match = p[idx_p] == '.' or p[idx_p] == s[idx_s]
                skip = check(idx_s, idx_p + 2)
                use = current_match and check(idx_s + 1, idx_p)
                return skip or use
            elif p[idx_p] == '.' or p[idx_p] == s[idx_s]:
                return check(idx_s + 1, idx_p + 1)
            else:
                return False
                   
        return check(0, 0)