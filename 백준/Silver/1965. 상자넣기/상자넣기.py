import sys

input = sys.stdin.readline



N = int(input())
arr = list(map(int,input().split()))
lis = []
lis.append(arr[0])

for i in range(N) :
    left = 0
    right = len(lis) - 1

    if lis[right] < arr[i] :
        lis.append(arr[i])
    else :
        while left <= right :
            mid = (left + right) // 2
            if lis[mid] > arr[i] :
                right = mid - 1
            elif lis[mid] < arr[i] :
                left = mid + 1
            else :
                left = mid
                break
        lis[left] = arr[i]
print(len(lis))