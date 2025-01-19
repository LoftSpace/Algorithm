def solution(s):
    N = len(s)
    answer = 1000000
    if N == 1 :
        return 1
    for length in range(1,N + 1):
        S = list(s)
        arr = []
        temp = S[:length]
        
        count = 0
        while S :
            if length <= len(S):
                # 현재 기준 문자열과 같다
                if temp == S[:length]:
                    
                    count += 1
                    for i in range(length):
                        S.pop(0)
                    if not S :
                        arr.append(str(count))
                        for i in temp :
                            arr.append(i)
                #다르다
                else :
                    #새로운 문자열에 추가
                    if count >1 :
                        arr.append(str(count))
                    for i in temp:
                        arr.append(i)
                    #기준 문자열 변경
                    temp = S[:length]
                    for i in range(length):
                        S.pop(0)
                    count = 1
                    if not S :
                        if count > 1:
                            arr.append(str(count))
                        for i in temp :
                            arr.append(i)
            else :
                if count > 1 :
                        arr.append(str(count))
                for i in temp :
                    arr.append(i)
                for i in S:
                    arr.append(i)
                    S.pop(0)
                break
        if S :
            for i in S:
                arr.append(i)
        #print(''.join(arr))
        answer = min(answer,len(''.join(arr)))
    
    return answer