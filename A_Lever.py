import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        cnt =0

        for i in range(n):
            cnt +=max(a[i] - b[i], 0)
        print(cnt+1)
if __name__ == "__main__":
    main()