def solution(sticker):
    N = len(sticker)
    answer = 0
    if N < 4 :
        return max(sticker)
    
    #첫 원소 선택한 경우
    dp1 = [[0] * 2 for _ in range(N)]
    dp1[2][1] = sticker[2]
    dp1[2][0] = 0
    for i in range(3,N-1):
        dp1[i][0] = max(dp1[i-1][1],dp1[i-1][0])
        dp1[i][1] = dp1[i-1][0] + sticker[i]
    
    answer = max(dp1[-2]) + sticker[0]
    
    #선택 안한경우
    dp2 = [[0] * 2 for _ in range(N)]
    dp2[1][1] = sticker[1]
    dp2[1][0] = 0
    for i in range(1,N):
        dp2[i][0] = max(dp2[i-1][1],dp2[i-1][0])
        dp2[i][1] = dp2[i-1][0] + sticker[i]
    answer = max(max(dp2[-1]),answer)
   
    return answer