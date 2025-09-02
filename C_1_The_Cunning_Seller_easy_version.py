import sys
input = sys.stdin.readline

def sum(n: int) -> int:
    ts = 0
    while n:
        n, r = divmod(n,3)
        ts+= r
    return ts

def main():
    t = int(input())
    p3 = [3**i for i in range(40)]

    for _ in range(t):
        n = int(input())
        s = sum(n)
        m = (n-s) // 2
        cnt = [n]
        add,x = 0,0

        while m:
            if x == len(cnt):
                cnt.append(0)
            left = cnt[x] // 3
            if not left:
                x += 1
                continue

            tk = min(left, m)
            add += tk * p3[x]
            cnt[x] -= tk * 3

            if x + 1 == len(cnt):
                cnt.append(0)
            cnt[x + 1] += tk
            m -= tk

        print(3 * n + add)

if __name__ == "__main__":
    main()
