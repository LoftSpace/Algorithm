def solution(s):
    def find(left,right,length):     
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            length += 2
        return length
    a = 0
   
    answer = 1
    if len(s) < 2 or s == s[::-1]:
        return len(s)
    
    for i in range(1,len(s)-1):
        answer = max(find(i,i+1,0),answer,find(i-1,i+1,1))
        
    answer = max(answer,find(0,1,0))

    return answer