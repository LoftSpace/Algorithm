N , D = map(int,input().split())
dp = [i for i in range(D + 1)]
shortcuts = [[] for _ in range(D  + 1)]

for i in range(N):
    start, end, distance = map(int,input().split())
    if start <= D and end <= D:
        shortcuts[start].append([end,distance])

for i in range(D):
    for j in shortcuts[i]:
        start = i
        end = j[0]
        d = j[1]
        for k in range(end,D + 1):
            if k <= D :
                dp[k] = min(dp[k],dp[i] + j[1] + k - j[0])

print(dp[-1])
