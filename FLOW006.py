t = int(input())
for i in range(0,t):
    n = input()
    l = 0
    for j in range(0, len(n)):
        l = l + int(n[j])
    print(l)
