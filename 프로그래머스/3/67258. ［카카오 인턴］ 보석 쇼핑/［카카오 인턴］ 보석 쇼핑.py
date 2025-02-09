def solution(gems):
    answer = [0,1000000]
    gems_set = set(gems)
    left = 0
    right = 0
    N = len(gems)
    temp = dict()
    temp[gems[0]] = 1
    
    def enough():
        for i in gems_set :
            if i not in temp or temp[i] == 0:
                return False
        return True
  
    while left <= right :
        #부족
        if not len(temp) == len(gems_set):
            #범위 체크
            if right < N - 1:
                right += 1
                #right포인터 한칸 늘리고 집합에 포함시키기
                if gems[right] in temp :
                    temp[gems[right]] += 1
                else :
                    temp[gems[right]] = 1
            else :
                break
        # 해당 구간이 모든 보석 포함
        else:
            #해당 구간이 저장해놓은 구간보다 더 짧다면 
            if answer[1] - answer[0] > right - left:
                #갱신
                answer[0] = left + 1
                answer[1] = right + 1
            #left 포인터 한칸 늘리고 temp에서 제외
            temp[gems[left]] -= 1
            if temp[gems[left]] == 0 :
                del temp[gems[left]]
            left += 1
        
    return answer