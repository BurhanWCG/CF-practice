import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        a.sort()
        ok = False
        for i in range(1,n):
            if a[i] == a[i-1]:
                ok = True
                break
        if ok:
            print("YES")
        else:
            print("NO")
if __name__ == "__main__":
    main()
