import sys
input = sys.stdin.readline

def solve():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        s = input().strip()
        pr = [0]
        for c in s:
            pr.append(pr[-1]+(c == '0'))

        ok = True
        for i in range(n - k + 1):
            if pr[i + k]-pr[i] == 0: 
                ok = False
                break

        if not ok:
            print("NO")
            continue
        c1 = s.count('1')
        a, b = 1, c1 + 1
        res = []

        for c in s:
            if c == '1':
                res.append(a)
                a += 1
            else:
                res.append(b)
                b += 1

        print("YES")
        print(*res)

def main():
    solve()

if __name__ == "__main__":
    main()
