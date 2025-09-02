import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        b = list(map(int, input().split()))

        mn = b[0]
        f = True
        for i in range(1, n):
            if b[i] % 2 == 0:
                big = (b[i] + 2)//2
            else:
                big = (b[i] + 1)//2

            if big > mn:
                f = False
                break
            mn = min(mn, b[i])

        if f:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()
