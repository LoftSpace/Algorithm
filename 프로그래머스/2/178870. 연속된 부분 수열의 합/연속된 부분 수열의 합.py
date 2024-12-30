def solution(sequence, k):
    N = len(sequence)
    arrSum = [0] * (N + 1)
    for i in range(N):
        arrSum[i + 1] = arrSum[i] + sequence[i]
  
    
    left = 1
    right = 1
    
    length = 1000000
    startIndex = 1000000
    endIndex = 1000000
    while right <= N :
        if arrSum[right] - arrSum[left-1] == k :
            if right - left < length :
                length = right - left
                startIndex = left - 1
                endIndex = right - 1
            elif right - left == length :
                if left - 1 < startIndex :
                    startIndex = left - 1
                    endIndex = right - 1
            right += 1
        elif arrSum[right] - arrSum[left-1] < k :
            right += 1
        else :
            left += 1
    answer = []
    answer.append(startIndex)
    answer.append(endIndex)
    return answer