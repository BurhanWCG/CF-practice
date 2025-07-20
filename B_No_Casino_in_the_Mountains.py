import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        
        cnt = 0
        i = 0
        while i <=n - k:
            if all(a[i + j] ==0 for j in range(k)):
                cnt+= 1
                i+= k + 1 
            else:
                i+= 1
        print(cnt)

if __name__ == "__main__":
    main()
