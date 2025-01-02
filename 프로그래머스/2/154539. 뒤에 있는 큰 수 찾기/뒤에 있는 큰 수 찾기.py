def solution(numbers):
    N = len(numbers)
    arr = [i for i in range(N)]
    
    answer = [0] * (N)
    for i in range(N-2,-1,-1) :
        if numbers[i] >= numbers[i + 1] :
            j = i + 1
            flag = False
            while numbers[j] <= numbers[i] :
                #뒤큰 수 없음
                if j == arr[j] :
                    arr[i] = -1
                    flag = True
                    break
                else :
                    j = arr[j]
            if not flag :
                arr[i] = j
        #다음 원소가 뒤큰수 이면
        else :
            arr[i] = i + 1
    arr[-1] = -1
    
    for i in range(N) :
        if arr[i] != -1 :
            answer[i] = numbers[arr[i]]
        else :
            answer[i] = -1
    return answer