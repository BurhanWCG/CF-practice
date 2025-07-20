import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        x = int(input())
        d = set(str(x)) 
        for y in range(1001):
            if d & set(str(y)):
                print(y)
                break

if __name__ == "__main__":
    main()
