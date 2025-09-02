import sys
input = sys.stdin.readline

def solve(n, k, a):
    ops = float('inf')
    if k in [2, 3, 5]:
        zero = False
        for x in a:
            if x % k == 0:
                zero = True
        if zero:
            return 0
        for x in a:
            inc = (k - x % k) % k
            ops = min(ops, inc)
        return ops
    else:  
        if n == 1:
            return (4 - a[0] % 4) % 4
        cnt = 0
        zero = False
        single = 4
        for x in a:
            if x % 4 == 0:
                zero = True
            elif x % 2 == 0:
                cnt += 1
            single = min(single, (4 - x % 4) % 4)
        if zero:
            return 0
        return min(single, max(0, 2 - cnt))

def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        print(solve(n, k, a))

if __name__ == "__main__":
    main()