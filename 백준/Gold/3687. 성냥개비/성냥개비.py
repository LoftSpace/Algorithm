import sys

input = sys.stdin.readline
T = int(input())
init_list = ['','',1,7,4,2,0,8]
INF = float('inf')
dp = [INF] * 101
for i in range(2,8):
    dp[i] = init_list[i]
dp[6] = 6

for i in range(8,101):
        for j in range(2,8):
            dp[i] = min(dp[i],dp[i-j] * 10 + init_list[j])

for test in range(T):
    n = int(input())
    answer_max = '7' * (n % 2) + '1' * (n // 2 - (n % 2))
    Min = dp[n]
    print(Min,int(answer_max))
    
