import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        cnt = 0
        x = a[0]
        for i in range(1, n):
            y = a[i]
            if abs(y)>abs(x):
                cnt += 1
        if cnt>= (n - 1) // 2:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()
