# Problem link: https://codeforces.com/problemset/problem/1742/A

t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())
    if a == b + c or b == c + a or c == a + b:
        print("YES")
    else:
        print("NO")
        