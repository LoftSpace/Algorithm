import math
def solution(r1, r2):
    answer = 0
    
    for x in range(1,r2+1):
        end = math.floor(math.sqrt((r2 ** 2 - x ** 2)))
        if x >= r1 :
            start = 0
        else :
            start = math.ceil(math.sqrt((r1 ** 2 - x ** 2)))
        answer += end - start + 1
   
    
    
    answer *= 4
   

     
    return answer