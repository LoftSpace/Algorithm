from collections import deque
def solution(progresses, speeds):
    answer = []
    temp = 0
    queue = deque(progresses)
    speeds = deque(speeds)
    while queue :
        for i in range(len(queue)):
            queue[i] += speeds[i]
        i = 0
        if queue[0] >= 100 :
            count = 0
            while queue and queue[0] >= 100 :
                queue.popleft()
                speeds.popleft()
                count += 1
                i += 1
            answer.append(count)
    
    return answer