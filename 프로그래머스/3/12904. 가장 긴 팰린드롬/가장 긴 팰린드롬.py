def solution(S):
    s = []
    for i in S :
        s.append('#')
        s.append(i)
    s.append('#')
    r = 0
    p = 0
    dp = [0] * (len(s))
    for i in range(len(s)):
        
        if i <= r and i + dp[2*p-i] <= r:
            dp[i] = dp[2*p-i]
        elif i <= r and i + dp[2*p-i] > r :
            dp[i] = r - i
        else :
            dp[i] = 0
        
        while i - dp[i] - 1 >= 0 and i + dp[i] + 1 < len(s) and s[i + dp[i] + 1] == s[i - dp[i] - 1] :
            dp[i] += 1
        
        if i + dp[i] > r :
            r = i + dp[i]
            p = i
    
    answer = max(dp)
    return answer