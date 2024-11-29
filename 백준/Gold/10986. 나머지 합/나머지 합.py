import sys

N, M = map(int,input().split())
ans = 0
arr = list(map(int,input().split()))
arrSum = [0]
Sum = 0

for i in range(len(arr)) :
    Sum += arr[i]
    arrSum.append(Sum)

arr2 = [0] * M

for i in arrSum :
    arr2[i%M] += 1
arr2[0] -= 1



for i in arr2 :
    ans += i * (i-1) // 2
ans += arr2[0]

print(ans)