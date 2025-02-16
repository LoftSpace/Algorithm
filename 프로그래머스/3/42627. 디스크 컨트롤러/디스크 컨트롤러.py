import heapq
from collections import deque
def solution(jobs):
    answer = 0
    jobs.sort(key = lambda x: [x[0],x[1]])
    job_queue = deque(jobs)
    waiting_queue = []
    heapq.heapify(waiting_queue)
    job_num = 0
    wt = 0
    #첫 작업 다루기
    first_job = job_queue.popleft()
    time = first_job[0]
    heapq.heappush(waiting_queue,[first_job[1],first_job[0],job_num])
    job_num += 1
    
    while job_queue or waiting_queue:
        # 작업 처리
        if waiting_queue :
            job = heapq.heappop(waiting_queue)
            # 시간 갱신
            if time < job[1] :
                time = job[1] + job[0]
            else :
                time += job[0]
            #대기 시간 갱신
            wt += (time - job[1])
            
        else :
            time = job_queue[0][0]
            
        # 작업큐에 들어 올 수 있는 작업들 추가
        while job_queue and job_queue[0][0] <= time :
            new_job = job_queue.popleft()
            heapq.heappush(waiting_queue,[new_job[1],new_job[0],job_num])
            job_num += 1
        
    #print(wt)
    answer = wt // len(jobs)
    return answer