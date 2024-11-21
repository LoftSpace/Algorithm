import sys

input = sys.stdin.readline

N , M = map(int,input().split())

arr = list(map(int,input().split()))
arr2 = [0] * (N+1)
for i in range(1,N + 1) :
    arr2[i] = arr2[i-1] + arr[i-1]


for testcase in range(M) :
    i , j = map(int,input().split())
    print(arr2[j] - arr2[i-1])