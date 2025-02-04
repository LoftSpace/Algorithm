def solution(triangle):
    N = len(triangle)
    dp = [[0] * i for i in range(1,N + 1)]
    
    dp[0][0] = triangle[0][0]

    # i 층
    for i in range(1,N):
        # 총 i + 1개 원소
        for j in range(i + 1):
            # 첫 원소
            if j == 0 :
                dp[i][j] = dp[i-1][0] + triangle[i][0]
            # 마지막 원소
            elif j == i :
                dp[i][j] = dp[i-1][-1] + triangle[i][-1]
            #그 사이
            else :
                dp[i][j] = max(dp[i-1][j-1],dp[i-1][j]) + triangle[i][j]
    
    answer = max(dp[-1])
    return answer