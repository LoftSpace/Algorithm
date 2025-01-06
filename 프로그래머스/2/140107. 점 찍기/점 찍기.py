def solution(k, d):
    answer = 0
    count = 0
    for y in range(0,d + 1,k):
        x = (d **2 - y ** 2) ** (1/2)
        answer += ( x // k + 1)
    
    return answer