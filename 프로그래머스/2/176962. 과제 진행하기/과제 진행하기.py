
def solution(plans):
    plans.sort(key = lambda x:x[1])
    stack = []
    print(plans)
    answer = []
    for i in range(len(plans)) :
        currentPlan = plans[i]
        startTime = int(currentPlan[1][:2]) * 60 + int(currentPlan[1][3:])
        executionTime = int(currentPlan[2])
        endTime = (startTime + executionTime) 
        nextPlan = 0
        nextStartPlan = 0
        
        if i < len(plans) - 1 :
            nextPlan = plans[i + 1]
            nextStartTime = int(nextPlan[1][:2]) * 60 + int(nextPlan[1][3:])
            
            #다음 과제 전에 끝낼 수 없다
            if endTime > nextStartTime :
                stack.append([currentPlan[0], endTime - nextStartTime])
            # 다음과제 전에 끝낼 수 있다.
            else :
                answer.append(currentPlan[0])
                remainTime = nextStartTime - endTime
                if remainTime > 0 :
                    while remainTime > 0 and stack:
                        #남아있는 시간 동안 중단되었던 과제를 모두 끝낼 수 있을 경우
                        if stack[-1][1] <= remainTime :
                            name, time = stack.pop()
                            answer.append(name)
                            remainTime -= time
                        else :
                            stack[-1][1] -= remainTime
                            remainTime = 0
    #마지막 과제 넣고 큐에있는거 순서대로
    answer.append(plans[-1][0])
    while stack :
        name, time = stack.pop()
        answer.append(name)
   
    return answer