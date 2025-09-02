import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        vc = list(map(int, input().split()))
        skp = 0
        frnd = True
        i = 0
        while i < n:
            if frnd:
                if i + 1 <n and vc[i] == 0 and vc[i + 1] == 0:
                    i += 1
                elif i + 1 < n and vc[i] == 1 and vc[i +1] == 0:
                    i += 1
                    skp += 1
                elif i + 1< n and vc[i] ==1 and vc[i + 1]==1:
                    skp += 1
                elif vc[i]== 1:
                    skp += 1
                frnd = False
            else:
                i += 1
                frnd = True
            i += 1
        print(skp)

if __name__ == "__main__":
    main()
