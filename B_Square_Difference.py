import sys
import math

input = sys.stdin.readline

def is_prime(num: int) -> bool:
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    limit = int(math.sqrt(num)) + 1
    for i in range(3, limit, 2):
        if num % i == 0:
            return False
    return True

def main():
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        if a - b== 1:
            s = math.sqrt(a+ b)
            r = int(s)
            if r == s:
                print("NO")
            else:
                if is_prime(a + b):
                    print("YES")
                else:
                    print("NO")
        else:
            print("NO")

if __name__ == "__main__":
    main()
