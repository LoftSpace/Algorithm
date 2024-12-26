import sys

input = sys.stdin.readline

C , N = map(int,input().split())

cities = [list(map(int,input().split())) for _ in range(N)]
dp = [1e7 for _ in range(C  +100)]
dp[0] = 0
for cost, numPeople in cities : 
    for i in range(numPeople, C + 100) :
        dp[i] = min(dp[i-numPeople] + cost , dp[i])
print(min(dp[C:]))
