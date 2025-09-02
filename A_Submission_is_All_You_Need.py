import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = list(map(int, input().split()))

        f = [0] * 55  
        for i in s:
            f[i] += 1
        ans = 0
        cnt2 = min(f[0],f[1]) 
        ans += cnt2*2
        f[0]-=cnt2
        f[1] -=cnt2
        cnt1=f[0]  
        ans +=cnt1
        f[0] -=cnt1
        for i in range(55):
            if f[i]>0:
                ans+=i*f[i]
        print(ans)

if __name__ == "__main__":
    main()
