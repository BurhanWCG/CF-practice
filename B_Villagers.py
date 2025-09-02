import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        a.sort()
        ans =0
        if n%2 == 0:
            s = 1
        else:
            s = 0
        for i in range(s,n,2):
            ans +=a[i]
        print(ans)

if __name__ == "__main__":
    main()
