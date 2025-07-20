import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        s= input().strip()
        x = s.count('0')
        y = s.count('1')
        d = abs(x-y)//2

        if k<d:
            print("NO")
        elif (k-d)%2==0:
            print("YES")
        else:
            print("NO")
if __name__ == "__main__":
    main()