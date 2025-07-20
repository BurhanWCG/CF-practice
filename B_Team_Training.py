import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n, x = map(int, input().split())
        a = list(map(int, input().split()))
        a.sort(reverse=True)

        cnt = 0
        group_size = 0

        for i in range(n):
            group_size += 1
            if a[i] * group_size >= x:
                cnt += 1
                group_size = 0 

        print(cnt)

if __name__ == "__main__":
    main()
