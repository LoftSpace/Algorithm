from collections import deque
def solution(s):
    answer = 0
    for i in range(len(s)):
        queue = deque(s)
        stack = []
        for j in range(i):
            temp = queue.popleft()
            queue.append(temp)
        #print(queue)
        for i in queue :
            stack.append(i)
            while True :
                if len(stack) < 2 :
                    break
                elif stack[-1] == ')' and stack[-2] == '(':
                    stack.pop()
                    stack.pop()
                elif stack[-1] == '}' and stack[-2] == '{':
                    stack.pop()
                    stack.pop()
                elif stack[-1] == ']' and stack[-2] == '[':
                    stack.pop()
                    stack.pop()
                else :
                    break
        #print(stack)
        if not stack :
                answer += 1
            
    
    return answer