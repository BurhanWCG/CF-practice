import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        s = input().strip()
        n = len(s)
        cnt = 0
        ok = False
        for i in range(n):
            if s[i] == '(':
                cnt+=1
            else:
                cnt-=1
            if cnt==0 and i!=n-1:
                ok=True
        if ok:
            print("YES")
        else:
            print("NO")
            





if __name__ == "__main__":
    main()