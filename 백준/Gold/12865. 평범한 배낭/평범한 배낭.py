import sys

input = sys.stdin.readline

N , K = map(int,input().split())

W = [0]
V = [0]
dp = [[0] * (K + 1) for _ in range( N + 1 )]

for i in range(N):
    w , v = map(int,input().split())
    W.append(w)
    V.append(v)

for i in range(1, N + 1) :
    for w in range(1,K + 1):
        if W[i] <= w : # 전체 용량 초과 안한다면
                dp[i][w] = max(dp[i-1][w],dp[i-1][w-W[i]] + V[i])
        else :
            dp[i][w] = dp[i-1][w]

print(dp[N][K])