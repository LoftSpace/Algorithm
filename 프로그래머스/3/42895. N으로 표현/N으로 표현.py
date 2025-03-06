from collections import deque
def solution(N, number):
    dp = [[] for _ in range(9)]
    dp[1].append(N)
    hash = dict()
    hash[N] = 1
    
    for i in range(2,9):
        if dp[i-1][0] * 10 + N not in hash :
            dp[i].append(dp[i-1][0] * 10 + N)
            hash[dp[i-1][0] * 10 + N] = i
        for  j in range(1,i//2 + 1):
            for k in dp[j] :
                for l in dp[i - j]:
                    
                    if k + l not in hash :
                        dp[i].append(k + l)
                        hash[k + l] = i
                    if l - k not in hash :
                        dp[i].append(l - k)
                        hash[l - k] = i
                    if k * l not in hash :
                        dp[i].append(k * l)
                        hash[k * l] = i
                    if k - l not in hash :
                        dp[i].append(k - l)
                        hash[k - l] = i
                    
                    if k != 0 :
                        if l // k not in hash: 
                            dp[i].append(l // k)
                            hash[l//k] = i
                    if l != 0 :
                        if k // l not in hash :
                            dp[i].append(k // l)
                            hash[k // l] = i

    if number in hash :
        return hash[number]
    answer = -1
    return answer