import sys
input = sys.stdin.readline
def solve():
    t = int(input())
    for _ in range(t):
        n, k, b, s = map(int, input().split())
        ans = [0]*n

        if s<b*k or s>b*k+n*(k -1):
            print(-1)
            continue

        rem = s-b*k
        ans[0] = b * k

        for i in range(1,n):
            if rem >= k - 1:
                ans[i] = k -1
                rem -= (k -1)
            else:
                ans[i] = rem
                rem = 0
                break
        print(*ans)
def main():
    solve()

if __name__ == "__main__":
    main()
