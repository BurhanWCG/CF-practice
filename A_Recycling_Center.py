import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n, c = map(int, input().split())
        a = list(map(int, input().split()))
        cnt = 0
        
        for _ in range(n):
            mx = -1  
            mn = float('inf') 
            idx_mx = -1  
            idx_mn = -1  
            
            for i in range(len(a)):
                if a[i]<=c and a[i]> mx:
                    mx = a[i]
                    idx_mx = i
                if a[i]> c and a[i]< mn:
                    mn = a[i]
                    idx_mn= i
            
            if idx_mx!=-1:
                a.pop(idx_mx)
            else:
                a.pop(idx_mn)
                cnt +=1
            for i in range(len(a)):
                a[i] *=2
        print(cnt)

if __name__ == "__main__":
    main()