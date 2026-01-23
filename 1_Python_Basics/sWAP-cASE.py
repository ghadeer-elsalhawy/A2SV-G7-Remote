# Problem Link: https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true

def swap_case(s):
    res = ""
    for a in s:
        if a.isupper():
            res += a.lower()
        elif a.islower():
            res += a.upper()
        else:
            res += a
    return res

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
