import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = [0] * n
        left, right = 0, n - 1
        current = 1
        while left <= right:
            if left == right:
                arr[left] = current
            else:
                arr[left] = current
                arr[right] = current + 1
                current += 2
            left += 1
            right -= 1
        print(*arr)

if __name__ == "__main__":
    main()