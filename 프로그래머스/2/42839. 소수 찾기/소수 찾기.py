from itertools import permutations
import math
def solution(numbers):
    answer = 0
    N = len(numbers)
    arr = set()
    numbers = list(numbers)
    
    for i in range(1,N + 1):
        cases = list(permutations(numbers,i))
        for case in cases :
            arr.add(int(''.join(list(case))))
    if 1 in arr :
        arr.remove(1)
    if 0 in arr :
        arr.remove(0)
    for i in arr :
        flag = True
      
        for j in range(2,math.floor(math.sqrt(i)) + 1):
    
            if i % j == 0 :
                flag = False
                break
        if flag :
            answer += 1
    
    
    
   
    
    #print(arr)
    
    return answer