import sys

input = sys.stdin.readline

ans = []
T = int(input())
T_list = list(map(int,input().split()))

O = int(input())
O_list = list(map(int,input().split()))

dp = [[False] * (40001) for _ in range(T + 1)]

for i in range(T + 1):
    dp[i][0] = True
for i in range(T) :
    dp[i+1][T_list[i]] = True
for i in range(1, T + 1) :
    for j in range(1,40001) :
        currentWeight = T_list[i - 1]
        if dp[i-1][j] :
            dp[i][j] = True

        
        if dp[i-1][abs(j-currentWeight)] :
            dp[i][j] = True

        if j + currentWeight <= 40000 :
            if dp[i-1][j + currentWeight] :
                dp[i][j] = True

for i in O_list :
    if dp[T][i] :
        ans.append('Y')
    else :
        ans.append('N')

for i in range(len(ans) - 1) :
    print(ans[i],end = '')
    print(' ',end = '')
print(ans[-1])