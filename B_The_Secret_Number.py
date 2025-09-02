import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        ans = []
        p = 10
        for k in range(1, 19):
            d = p+1
            if d !=0 and n%d == 0:
                ans.append(n//d)
            if k < 18:
                p*= 10
        if not ans:
            print(0)
        else:
            ans.sort()
            print(len(ans))
            print(*ans)
if __name__ == "__main__":
    main()
