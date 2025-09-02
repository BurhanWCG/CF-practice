import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        presum = [0] * n
        presum[0] = a[0]
        for i in range(1, n):
            presum[i] = a[i] + presum[i - 1]

        bmax = 0
        ans = 0
        x = k
        k -= 1
        for i in range(n):
            if x == 0:
                break
            bmax = max(bmax, b[i])
            ans = max(ans, presum[i] + bmax*(k - i))
            x -= 1

        print(ans)

if __name__ == "__main__":
    main()
