n, t = map(int, input().split())

books = list(map(int, input().split()))

left = 0
maxi = 0
cur = 0

for right in range(n):
    cur += books[right]
    while cur > t:
        cur -= books[left]
        left += 1
    maxi = max(maxi, right - left + 1)

print(maxi)