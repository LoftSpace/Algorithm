def solution(n, money):
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in money :
        for j in range(1,n + 1):
            if j - i >= 0:
                dp[j] += dp[j - i]
    answer = dp[n]
    return answer