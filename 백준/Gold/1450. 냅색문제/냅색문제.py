import sys
from itertools import combinations

sys.setrecursionlimit(100000)

N,C = map(int,input().split())

arr = list(map(int,input().split()))

arr1 = arr[:N//2]
arr2 = arr[N//2:]


sub1 = [0]
sub2 = [0]

for i in range(1,len(arr1) + 1):
    for j in combinations(arr1,i):
        sub1.append(sum(j))

for i in range(1, len(arr2) + 1):
    for j in combinations(arr2,i):
        sub2.append(sum(j))


sub1.sort()
sub2.sort()


lengthOfSub2 = len(sub2)
count = 0
for i in sub1 :
    
    if i > C :
        continue

    left = 0
    right = lengthOfSub2 - 1
    
    while left <= right :
        mid = (left + right) // 2

        if i + sub2[mid] > C :
            right = mid-1
        else : 
            left = mid + 1
    
    count += (right+1)
print(count)
