import sys
from collections import deque
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = input().strip()
        m = int(input())
        b = input().strip()
        c = input().strip()

        d = deque(a)
        for i in range(m):
            if c[i] == 'V':
                d.appendleft(b[i])
            else:
                d.append(b[i])

        print(''.join(d))

if __name__ == "__main__":
    main()
