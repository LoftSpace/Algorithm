import sys

input = sys.stdin.readline

N = int(input())

arr = list(map(int,input().split()))
hash = dict()

for i in arr : 
    hash[i] = 1
M = int(input())

arr2 = list(map(int,input().split()))

ans = []
for i in arr2 :
    if i in hash :
        ans.append(1)
    else :
        ans.append(0)
print(*ans)