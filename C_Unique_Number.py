import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        x = int(input())
        if x > 45:
            print(-1)
        else:
            digits = []
            for d in range(9, 0, -1):
                if x >= d:
                    digits.append(d)
                    x -= d
            digits.sort()
            print(''.join(map(str, digits)))

if __name__ == "__main__":
    main()
