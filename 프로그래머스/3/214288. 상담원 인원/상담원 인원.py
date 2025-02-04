import heapq
from itertools import *
def solution(k, n, reqs):
    answer = 10000000
    schedule = [[] for _ in range(k)]
    for req in reqs :
        schedule[req[2]-1].append([req[0],req[1]])
        
    cases = set()
    #한 유형은 1~n-k+1개의 멘토 가질 수 있음
    for combination in combinations_with_replacement(range(1,n-k+2),k):
        #멘토는 총 n명
        if sum(combination) == n :
            #유형 부여
            for perm in permutations(combination,k):
                cases.add(perm)
    
    #각 경우에 대해
    for case in cases:
 
        waiting_time = 0
        #각 유형에 대해
        for category,mentor_num in enumerate(case):
       
   
            mentor = [0] * mentor_num
            heapq.heapify(mentor)
            for st,dt in schedule[category]:
                prev = heapq.heappop(mentor)
                if prev > st :
                    waiting_time += (prev - st)
                    heapq.heappush(mentor,prev + dt)
                else :
                    heapq.heappush(mentor,st + dt)
      
        answer = min(answer,waiting_time)
            
    return answer