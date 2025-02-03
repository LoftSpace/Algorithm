def solution(temperature, t1, t2, a, b, onboard):
    N = len(onboard)
    dp = [[1000000] * 51 for _ in range(N+1)]
    t1 += 10
    t2 += 10
    temperature += 10
    dp[0][temperature] = 0
    
    for i in range(0,N):
        start = 0
        end = 0
        if onboard[i] == 1 :
            start = t1 
            end = t2 
        else :
            start = 0
            end = 50
        
        for j in range(start,end + 1) :
        
            #온도 올리기
            # 에어컨 사용해서 올리기
            if j + 1 <= 50 and temperature <= j:
                dp[i + 1][j + 1] = min(dp[i + 1][j + 1],dp[i][j] + a)
            # 자동으로 올라감 
            if j + 1 <= 50  and j < temperature :
                dp[i + 1][j + 1] = min(dp[i + 1][j + 1],dp[i][j])
            
            #온도 그대로
            dp[i + 1][j] = min(dp[i + 1][j],dp[i][j] + b)
            
            #온도 내리기
            #에어컨 사용해서 내리기
            if j - 1 >= 0 and temperature >= j:
                dp[i + 1][j - 1] = min(dp[i + 1][j - 1],dp[i][j] + a)
            #자동으로 내려감
            if j - 1 >= 0 and temperature < j :
                dp[i + 1][j - 1] = min(dp[i + 1][j - 1],dp[i][j])
            
            #온도가 같다
            if j == temperature :
                dp[i + 1][j] =min(dp[i + 1][j],dp[i][j]) 
  
    answer = min(dp[-1])

    return answer