def solution(scores):
    answer = 0
    standards = []
    standards.append(scores[0][0])
    standards.append(scores[0][1])
    standard = scores[0][0] + scores[0][1]
    scores.sort(key = lambda x : [x[0],x[1]], reverse = True)
    
    cur_check = 1000000000
    cur_max = 0
    next_check = scores[0][0]
    next_max = scores[0][1]
    #print(scores)
    #print(cur_check,cur_max,next_check,next_max)
    for score in scores:
        #print(score)
        
        if score[0] > standards[0] and score[1] > standards[1] :
            return -1
        # 다음 단계 
        if score[0] != next_check:
            #업데이트
            cur_check = next_check
            cur_max = next_max
            next_check = score[0]
        #이전 단계 최소 조건보다 같거나 크다면(인센티브 받음)
        if score[1] >= cur_max :
            if standard < score[0] + score[1]:
                answer += 1
        # 다음 조건 업데이트 여부
        if score[1] > next_max :
            next_max = score[1]
        
        #print(cur_check,cur_max,next_check,next_max)
    return answer + 1