import sys

input = sys.stdin.readline

N = int(input())
arr=[]
lis = []
for i in range(N):
    arr.append(int(input()))

lis.append(arr[0])

for i in range(1,N):
    if lis[-1] < arr[i] :
        lis.append(arr[i])
    else :
        left = 0
        right = len(lis)
        while left <= right :
            mid = (left + right) // 2
            if lis[mid] == arr[i]:
                left = arr[i]
                break
            elif lis[mid] < arr[i] :
                left = mid + 1
            else :
                right = mid - 1
        lis[left] = arr[i]
print(N - len(lis))