import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        ans = 0
        arr.sort()

        while len(arr) > 1:
            j = len(arr)-1
            i = j-1 
            ans =  arr[i] + arr[j]-1
            arr.pop(j)
            arr.pop(i)
            arr.append(ans)

        print(arr[0])
            

if __name__ == "__main__":
    main()