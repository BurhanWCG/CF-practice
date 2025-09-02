import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = []
        if n % 2 != 0:
            for i in range(n):
                if i % 2 == 0:
                    a.append(-1)
                else:
                    a.append(3)
        else:
            if n == 2:
                a = [-1, 2]
            else:
                for i in range(n-2):
                    if i % 2 ==0:
                        a.append(-1)
                    else:
                        a.append(3)
                a.append(-1)
                a.append(2)
        print(*a)

if __name__ == "__main__":
    main()