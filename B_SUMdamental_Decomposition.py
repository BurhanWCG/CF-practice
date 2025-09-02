import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n, x = map(int, input().split())
        bc = bin(x).count('1') 
        
        if x == 0:
            if n == 1:
                print(-1)
            elif n % 2 == 0:
                print(n)
            else:
                print(n - 1 + 4)
        elif x == 1:
            if n == 2:  
                print(5)
            elif n % 2:
                print(n)
            else:
                print(n - 1 + 4)
        elif bc >= n:
            print(x)
        else:
            if (n - bc) % 2 == 0:
                print(x + n - bc)
            else:
                print(x + n - bc + 1)

if __name__ == "__main__":
    main()