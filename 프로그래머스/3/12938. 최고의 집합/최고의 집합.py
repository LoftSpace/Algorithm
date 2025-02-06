def solution(n, s):
    if s < n :
        return [-1]
    
    a = s // n
    elements = [a] * n
    remain = s % n
    i = 0
    
    while remain > 0 :
        elements[-1-i] += 1
        i += 1
        remain -=1
  
    for i in elements :
        if i == 0 :
            return [-1]
        
    answer = elements
    return answer