import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        cnt = 0
        for _ in range(n):
            a, b, c, d = map(int, input().split())
            zero= max(0, a - c)
            one= max(0, b - d)
            if b > d:
                cnt+= zero+ one+ (a - zero)
            else:
                cnt+= zero + one
        print(cnt)

if __name__ == "__main__":
    main()