import sys
from collections import Counter
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        s = list(map(int, input().split()))
        a = list(map(int, input().split())) 

        if k == 0:
            s.sort()
            a.sort()
            if s == a:
                print("YES")
            else:
                print("NO")
            continue

        cnt = Counter()
        for i in s:
            r = i% k
            if r <0:
                r += k
            mn = min(r, k-r)
            cnt[mn] += 1

        for j in a:
            r = j % k
            if r < 0:
                r +=k
            mn = min(r, k-r)
            cnt[mn] -=1

        ok = True
        for count in cnt.values():
            if count !=0:
                ok = False
                break

        if ok:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()
