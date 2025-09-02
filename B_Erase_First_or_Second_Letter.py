import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input().strip()
        st = set()
        ans = 0
        for i in range(n):
            if s[i] not in st:
                st.add(s[i])
            ans +=len(st)
        print(ans)

if __name__ == "__main__":
    main()