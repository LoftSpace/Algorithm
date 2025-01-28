from collections import deque
def solution(bridge_length, weight, truck_weight):
    queue = [0] * bridge_length
    truck_weights = deque(truck_weight)
    time_count = 0
    current_bridge_weight = 0
    
    def is_queue_empty():
        for i in queue :
            if i != 0 :
                return False
        return True
    
  
    while True :
        # 종료
        if is_queue_empty() and not truck_weights : 
            break
        
        time_count += 1
        current_bridge_weight -= queue[time_count % bridge_length]
        queue[time_count % bridge_length] = 0
        
        # 대기중인 트럭이 존재
        if truck_weights :
            # 다음 트럭 넣을 수 있다
            if truck_weights[0] + current_bridge_weight <= weight:
                current_bridge_weight += truck_weights[0]
                queue[time_count % bridge_length] = truck_weights.popleft()
        
        
    answer = time_count
    return answer