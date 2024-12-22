import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))

lis = []
lis.append(arr[0])

for i in range(1,N):
    if arr[i] > lis[-1] :
        lis.append(arr[i])
    else :
        left = 0
        right = len(lis) - 1
        while left <= right :
            mid = (left + right) // 2
            if lis[mid] == arr[i] :
                left = mid
                break
            elif lis[mid] > arr[i] :
                right = mid - 1
            else :
                left = mid + 1
        lis[left] = arr[i]
print(len(lis))