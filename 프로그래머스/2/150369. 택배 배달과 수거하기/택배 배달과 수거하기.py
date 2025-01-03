from collections import deque

def solution(cap, n, deliveries, pickups):
    answer = 0
    
    while True :
        while len(deliveries) > 0 and deliveries[-1] == 0 :
                deliveries.pop()
        while len(pickups) > 0 and pickups[-1] == 0 :
                pickups.pop()
                
        answer += max(len(deliveries),len(pickups)) * 2
        capacity = cap
        while capacity > 0 :
            # 배달 및 수거
            if len(deliveries) > 0 :
                    deliveries[-1] -= 1
            if len(pickups) > 0 :
                    pickups[-1] -= 1
            capacity -= 1
            
            while len(deliveries) > 0 and deliveries[-1] == 0 :
                    deliveries.pop()
            while len(pickups) > 0 and pickups[-1] == 0 :
                    pickups.pop()
        
        if len(pickups) == 0 and len(deliveries) == 0 :
            break
            
        
            
    return answer