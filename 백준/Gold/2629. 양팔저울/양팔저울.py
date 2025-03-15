import sys

input = sys.stdin.readline

N = int(input())
v = list(map(int,input().split()))
M = int(input())
m = list(map(int,input().split()))
MAX_RANGE = N * 500 + 1
dp = [[False] * MAX_RANGE for _ in range(N)]
dp[0][0] = True
dp[0][v[0]] = True

# 각 추에 대해
for i in range(1,N):
    for j in range(MAX_RANGE):
        if dp[i-1][j] :
            dp[i][j] = True
            continue
        elif dp[i-1][abs(j-v[i])]:
                dp[i][j] = True
                continue
        if j + v[i] < MAX_RANGE:
                dp[i][j] = dp[i-1][j + v[i]]

ans = []
#print(dp[3][8])
#print(dp[1][2])
for i in m :
    if i > MAX_RANGE : 
        ans.append('N')
    elif dp[N-1][i] :
        ans.append('Y')
    else :
        ans.append('N')

for i in range(len(ans) - 1) :
    print(ans[i],end = '')
    print(' ',end = '')

print(ans[-1])