import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input().strip()
        fg =0
        lst = [s[0],s[n-1]]
        for i in range(1,n-1):
            if s[i] in lst:
                fg = 1
                break
            else:
                lst.append(s[i])
        if(fg):
            print("Yes")
        else:
            print("No")

if __name__ == "__main__":
    main()