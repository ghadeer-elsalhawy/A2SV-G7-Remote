class Solution:
    def simplifyPath(self, path: str) -> str:

        sep = path.split("/")
        res = []
        # print(sep)
        for val in sep:
            if val == "..":
                if res:
                    res.pop()
            elif val == "." or val == "":
                continue
            else:
                res.append(val)
        if not res:
            return "/"
        else:
            tot = ""
            for r in res:
                tot += "/" + r
            return tot