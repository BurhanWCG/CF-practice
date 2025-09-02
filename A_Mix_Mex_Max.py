import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        s = set()
        for i in a:
            if i !=-1:
                s.add(i)
        if len(s) == 0:
            print("YES")
        elif len(s) > 1:
            print("NO")
        else:
            x = next(iter(s))
            if x > 0:
                print("YES")
            else:
                print("NO")

if __name__ == "__main__":
    main()
