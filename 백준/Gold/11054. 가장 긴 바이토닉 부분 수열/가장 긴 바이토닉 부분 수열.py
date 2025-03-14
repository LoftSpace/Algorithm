import sys

input = sys.stdin.readline

N = int(input())
Arr = list(map(int,input().split()))

answer = 1

def LIS(arr):
    lis = []
    lis.append(arr[0])
    n = len(arr)
    for i in range(1,n) :
        if arr[i] > lis[-1]:
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
    return len(lis)

reversed = Arr[::-1]

for i in range(N):
    left = 0
    right = 0
    if len(Arr[:i + 1]) > 0 :
        left = LIS(Arr[:i + 1])
    temp = Arr[i:]
    temp = temp[::-1]
    if len(temp) > 0 :
        right = LIS(temp)
    #print(left,right)
    answer = max(left+right-1,answer)
   
print(answer)
