import heapq
def solution(n, works):
    answer = 0
    heap = []
    heapq.heapify(heap)
    for i in works :
        heapq.heappush(heap,-i)
    for i in range(n):
        if heap : 
            a = heapq.heappop(heap)
            a += 1
            if a != 0 :
                heapq.heappush(heap,a)
    #print(heap)
    for i in heap :
        answer += (-i) ** 2
    
    return answer