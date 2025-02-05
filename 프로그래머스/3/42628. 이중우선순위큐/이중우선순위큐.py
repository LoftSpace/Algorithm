import heapq
def solution(operations):
    max_heap = []
    min_heap = []
    heapq.heapify(max_heap)
    heapq.heapify(min_heap)
    elements = set()
    #각 명령어에 대해
    for operation in operations :
        instructions = operation.split(" ")
        arg1 = instructions[0]
        arg2 = instructions[1] 
     
        
        # 삽입 이면
        if arg1 == 'I':
            #삽입
            heapq.heappush(max_heap,-int(arg2))
            heapq.heappush(min_heap,int(arg2))
            elements.add(int(arg2))
        
        # 삭제
        elif arg1 == 'D' :
            if not elements:
                continue
            # 최댓값 삭제
            if arg2 == '1' :
                #최대 힙에서 뺀게 집합에 있을 때 까지
                while True:
                    a = -heapq.heappop(max_heap)
                    # 찾는 그 값이다
                    if a in elements :
                        elements.remove(a)
                        break
                
            # 최솟값 삭제
            else :
                while True :
                    a = heapq.heappop(min_heap)
                    if a in elements :
                        elements.remove(a)
                        break
          
  
    if not elements :
        return [0,0]
    else :
        arr = list(elements)
        arr.sort()
        
        return [arr[-1],arr[0]]
    answer = []
    return answer