import sys
input = sys.stdin.readline


def main():
    t = int(input())
    for _ in range(t):
        n, j, k = map(int, input().split())
        a = list(map(int, input().split()))
        sa = sorted(a)
        sa = sa[n - k:]
        if j in sa:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()
