import sys
import copy
N = int(input())
arr = list(input().strip())
target = list(input().strip())
for i in range(N):
    target[i] = int(target[i])
    arr[i] = int(arr[i])
arr2 = copy.deepcopy(arr)
def change(i,arr):
    if i == len(arr) - 1 :
        if arr[i] == 0 :
            arr[i] = 1
        else :
            arr[i] = 0

        if arr[i-1] == 0 :
            arr[i-1] = 1
        else :
            arr[i-1] = 0
    else :
        if arr[i-1] == 0 :
            arr[i-1] = 1
        else :
            arr[i-1] = 0
        
        if arr[i] == 0 :
            arr[i] = 1
        else :
            arr[i] = 0

        if arr[i + 1] == 0 :
            arr[i + 1] = 1
        else :
            arr[i + 1] = 0
count1 = 0
# 0번 스위치 안누름
for i in range(1,N):
    if arr[i-1] != target[i-1]:
        change(i,arr)
        count1 += 1
ans = 1000000000

if arr == target :
    ans = min(ans,count1)
#print(arr)
count2 = 1


#0번 스위치 누름
if arr2[0] == 0 :
    arr2[0] = 1
else :
    arr2[0] = 0

if arr2[1] == 0 :
    arr2[1] = 1
else :
    arr2[1] = 0

for i in range(1,N):
    if arr2[i-1] != target[i-1]:
        
        change(i,arr2)
        count2 += 1
if target == arr2 :
    ans = min(ans,count2)

#print(arr2)
if ans != 1000000000 :
    print(ans)
else :
    print(-1)