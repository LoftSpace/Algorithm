from collections import deque
def solution(n, info):
    queue = deque([(0,[0,0,0,0,0,0,0,0,0,0,0])])
    max_gap = 0
    answer = []
    while queue :
        count, arrow = queue.popleft()
        # 화살 다쏨
        if sum(arrow) == n :
            ryan = 0
            apeach = 0
            for i in range(11):
                if not (arrow[i] == 0 and info[i] == 0):
                    if arrow[i] > info[i] :
                        ryan += 10 - i
                    else :
                        apeach += 10 - i
            if ryan > apeach :
                gap = ryan - apeach
                if max_gap < gap :
                    answer.clear()
                    max_gap = gap
                    answer.append(arrow)
                elif max_gap == gap :
                    answer.append(arrow)
        elif sum(arrow) > n:
            continue
            
        # 마지막 과녁 : 남은 화살 다 쓴다.
        elif count == 10 :
            temp = arrow.copy()
            temp[count] = n - sum(temp)
            queue.append((0,temp))
        else :
            # 현재 과녁 포함
            temp = arrow.copy()
            temp[count] = info[count] + 1
            queue.append((count + 1,temp))
            '''
            # 쏠 수 있으면
            if n - sum(temp) > info[count] :
                temp[count] = info[count] + 1
                if not sum(temp) > n :
                    queue.append((count + 1,temp))
            '''
            # 현재 과녁 안포함
            temp2 = arrow.copy()
            temp2[count] = 0
            queue.append((count + 1,temp2))
            

    if not answer :
        return [-1]
    elif len(answer) == 1 :
        return answer[0]
    else :
        return answer[-1]
   