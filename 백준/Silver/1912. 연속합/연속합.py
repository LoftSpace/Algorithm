import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))
answer = 0
dp = [0] * len(arr)
dp[0] = arr[0]
for i in range(1,len(arr)):
    if dp[i-1] < 0 :
        dp[i] = arr[i]
    else :

        dp[i] = dp[i-1] + arr[i]

print(max(dp))