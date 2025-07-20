import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        mn = min(n,m)
        if mn <= 2:
            print("NO")
        else:
            print("YES")

if __name__ == "__main__":
    main()