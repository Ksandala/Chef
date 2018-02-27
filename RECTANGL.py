import math
 
t = int(input())
for _ in range(t):
    a = list(sorted(map(int, input().split())))
    if a[1] == a[0] and a[2] == a[3]:
      print("YES")
    else:
      print("NO")
