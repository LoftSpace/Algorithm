def solution(stones, k):
    N = len(stones)
    #해당 명수가 다리를 지나갈 수 있는지 확인
    def can_pass(people):
        left = 0
        right = 0
        while right < N :
            if stones[right] <= people :
                right += 1
            else :
                if right - left >= k :
                    return right - left
                else :
                    left = right + 1
                    right = left
      
            
        return right - left
    
    people_range = max(stones)
    left = 1
    right = people_range
    
    while left <= right :
        mid = (left + right) // 2
        #print(left,right,mid)
        if can_pass(mid) >= k :
            right  = mid - 1
        else :
            left = mid + 1
        
    #print(can_pass(3))
    answer = left
    return answer