import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(2 * n - 1)
        print(1, 1, n)
        for i in range(2, n + 1):
            print(i, 1, i - 1)
            print(i, i, n)

if __name__ == "__main__":
    main()
