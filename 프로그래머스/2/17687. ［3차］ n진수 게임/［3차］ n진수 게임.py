def solution(n, t, m, p):
    answer = ''
    arr = '0'
    count= 0
    def convert(num,n):
        temp = ''
        while num :
            a = num % n
            if a >= 10 :
                temp += format(a,'X')
            else :
                temp += str(a)
            num = num // n
        return temp[::-1]
    
    
    for i in range(t*m):
        arr += convert(i,n)
    #print(arr)
    for j in range(p - 1,len(arr),m):
        count += 1
        answer += arr[j]
        if count == t :
            break
        
    
    
    return answer