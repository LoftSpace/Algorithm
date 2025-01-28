def solution(prices):
    stack = []
    N = len(prices)
    answer = [0] * N
    
    for i in range(0,N):
        if stack :
            # 더 큰거 삽입
            if stack[-1][0] <= prices[i]:
                for j in stack :
                    answer[j[1]] += 1
                stack.append([prices[i],i])
            # 작은거 삽입
            else :
                while stack and stack[-1][0] > prices[i] :
                    answer[stack[-1][1]] += 1
                    stack.pop()   
                for j in stack :
                    answer[j[1]] += 1
                stack.append([prices[i],i])
        else :
            stack.append([prices[i],i])
  
    
    return answer