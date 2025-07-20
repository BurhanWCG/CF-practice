import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    l = int(input())
    a = list(map(int, input().split()))
    found = False
    idx = -1
    for i in range(l - 1):
        if a[i] > a[i + 1]:
            idx = i
            found = True
            break
    if found:
        print("YES")
        print(2)
        print(a[idx], a[idx + 1])

    else:
        print("NO")