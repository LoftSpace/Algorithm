import sys

input = sys.stdin.readline

N , S , M = map(int,input().split())

V = list(map(int,input().split()))

dp = [[0] * (M + 1) for _ in range(N + 1)]
dp[0][S] = 1

for i in range(1, N + 1) :
    for j in range (M + 1) :
        if j - V[i-1] >= 0 :
            if dp[i-1][j - V[i-1]] == 1 :
                dp[i][j] = 1
        if j + V[i-1] <= M :
            if dp[i-1][j + V[i-1]] == 1 :
                dp[i][j] = 1
           
ans = []
for i in range(M  + 1) :
    if dp[N][i] == 1 :
        ans.append(i)
if len(ans) == 0 :
    print(-1)
else :
    print(max(ans))