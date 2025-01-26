from collections import deque
import heapq
def solution(priorities, location):
    count = 0
    queue = deque(priorities)
    heap = []
    heapq.heapify(heap)
    for i in priorities :
        heapq.heappush(heap,-i)
        
    while True :
        process = queue.popleft()
        # 큐에 더 큰게 있다면
        if -heap[0] > process :
            # 뒤로 보내기
            queue.append(process)
            if location == 0 :
                location = len(queue) - 1
            else :
                location -= 1
        else :
            # 실행
            # 타겟을 실행
            if location == 0 :
                return count + 1
            # 타겟이 아닌 것을 실행
            else :
                location -= 1
                count += 1
                heapq.heappop(heap)
            
    answer = count
    return answer