cost, dollars, bananas = map(int, input().split())

total = ((bananas + 1) * bananas // 2) * cost

res = (max(0, total - dollars))

print(res)
