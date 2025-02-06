
def solution(m, n, puddles):
    dp = [[0] * m for _ in range(n)]
    grid = [[0] * m for _ in range(n)]
    for i in puddles :
        grid[i[1]-1][i[0]-1] = 1
   
    i = 0
    while i < n and grid[i][0] != 1 :
        dp[i][0] = 1
        i += 1
    #각 col에 대해
    for j in range(1,m):
        #각 row에 대해
        for i in range(n):
            # 우물이 아니다
            if grid[i][j] != 1 :
                # 맨위의 장소
                if j == 0 :
                    # 왼쪽이 우물이 아니다
                    if grid[i-1][j] != 1 :
                        dp[i][j] += dp[i-1][j]
                
                else :
                    if grid[i][j-1] != 1 :
                        dp[i][j] += dp[i][j-1]
                    if grid[i-1][j] != 1 :
                        dp[i][j] += dp[i-1][j]
    #print(dp)
    answer = dp[-1][-1] % 1000000007
    return answer