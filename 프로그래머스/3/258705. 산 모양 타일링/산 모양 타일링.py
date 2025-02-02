def solution(n, tops):
    shape = [[1,1,0] for _ in range(n)]
    dp = [[0,0,0,0] for _ in range(n)]
    
    for i in range(len(tops)) :
        shape[i][2] = tops[i]
        
    dp[0][0] = 1
    dp[0][1] = 1
    dp[0][3] = 1
    
    if shape[0][2] == 1 :
        dp[0][2] = 1
    
    for i in range(1,n):
        Sum = sum(dp[i-1][j] for j in range(4)) % 10007
        #선택안함
        dp[i][0] = Sum
        #1번 모양 선택
        dp[i][1] = Sum - dp[i-1][3] 
        #2번 모양 선택
        if shape[i][2] != 0 :
            dp[i][2] = Sum
        #3번 모양 선택
        dp[i][3] = Sum 
    
    
    answer = sum(dp[n-1]) % 10007
    
    return answer