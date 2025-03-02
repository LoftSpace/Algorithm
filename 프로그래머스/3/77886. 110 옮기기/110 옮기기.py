from collections import deque
def solution(s):
    answer = []
    for element in s :
        
        count = 0
        N = len(element)
        arr = list(element)
        arr = deque(arr)
        stack = []
        while arr :
            stack.append(arr.popleft())
            if len(stack) > 2 :
                if stack[-1] == '0' and stack[-2] == '1' and stack[-3] == '1':
                    stack.pop()
                    stack.pop()
                    stack.pop()
                    count += 1
                    
        #print(stack)
        stack = ''.join(stack[::-1])
        idx = stack.find('0')
        
        if idx != -1 :
            res = stack[:idx] + "011" * count + stack[idx:]
        else :
            res = stack + '011' * count 
        #print(res)
        answer.append(res[::-1])
            
        
    
    
    return answer