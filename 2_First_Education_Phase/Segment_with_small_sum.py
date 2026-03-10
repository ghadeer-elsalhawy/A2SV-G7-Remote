n, s = map(int, input().split())

nums = list(map(int, input().split()))

left = 0

cur = 0

res = 0

for right in range(n):
    cur += nums[right]
    while cur > s:
        cur -= nums[left]
        left += 1
    res = max(res, right - left + 1)
print(res)
