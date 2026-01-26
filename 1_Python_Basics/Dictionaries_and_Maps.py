# Problem Link: https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem

import sys
t = int(input())
d = {}
for _ in range(t):
    k, v = input().split()
    d[k] = v
    
for l in sys.stdin:
    temp = l.strip()
    if temp in d:
        print(temp + "=" + d[temp])
    else:
        print("Not found")
      
