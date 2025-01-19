def solution(s):
    answer = []
    Max = 0
    arr = []
    hash = dict()
    s = s[1:-1]
    
    s = s[1:-1]
    
    s = s.split('},{')
   
    for i in s :
        temp = []
        i = i.split(',')
        
        arr.append(i)
  
   
    arr.sort(key = len)
   
    for elements in arr :
        for element in elements :
            if int(element) not in hash :
                hash[int(element)] = True
                answer.append(int(element))
    
    return answer