def solution(numbers):
    
    answer = []
    for number in numbers :
        a = list('0' + bin(number)[2:])
        
            
        
        for i in range(len(a)-1,-1,-1):
            if a[i] == '0' :
                a[i] = '1'
                break
        if number % 2 == 1 :
            a[i + 1] = '0'
        
        num = ''.join(a)
        answer.append(int(num,2))
    
    return answer