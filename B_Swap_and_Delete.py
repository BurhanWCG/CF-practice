import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        s = input().strip()

        cnt = [0, 0]
        for ch in s:
            cnt[int(ch)] += 1

        ans = 0
        for ch in s:
            o = int(ch)^1
            if cnt[o]:
                ans += 1
                cnt[o]-= 1
            else:
                break

        print(len(s)-ans)

if __name__ == "__main__":
    main()
