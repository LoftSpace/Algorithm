import heapq

def solution(a):
    answer = 0
    left_heap = []
    right_heap = []
    heapq.heapify(left_heap)
    heapq.heapify(right_heap)
    hash = dict()
    for i in a :
        heapq.heappush(right_heap,i)
        hash[i] = True
    
    for i in range(len(a)):
        #print(a[i])
        #마지막 원소 처리
        if not right_heap : 
            answer += 1
            continue
        
        while hash[right_heap[0]] == False:
            heapq.heappop(right_heap)
        # 오른쪽 힙 보다 작다면 생존 보장
        if right_heap[0] > a[i] :
            answer += 1
        # 같다면 생존보장, 자기 자기 자신pop
        elif right_heap[0] == a[i] :
            heapq.heappop(right_heap)
            answer += 1
            #print('오른쪽 힙이 자기 자신임')
        # 크다면 찬스 소모, 왼쪽 힙과 비교
        else :
            
            if left_heap :
                if left_heap[0] > a[i] :
                    answer += 1
                    #print('왼쪽 힙보다는 작음')
            # 왼쪽힙이 없다면 첫번째원소이므로 생존 보장
            else :
                #print('첫번째 원소')
                answer += 1
        heapq.heappush(left_heap,a[i])
        hash[a[i]] = False
    return answer