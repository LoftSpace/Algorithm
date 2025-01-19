import sys
sys.setrecursionlimit(10**6)
def solution(p):
    
    def isPerfect(p):
        stack = []
        for i in p :
            stack.append(i)
            if len(stack) >= 2:
                if stack[-1] == ')' and stack[-2] == '(' :
                    stack.pop()
                    stack.pop()
        if stack :
            return False
        return True
    
    def func(p):
        if p == '':
            return ''
        left = 0
        right = 0
        u = ''
        v = ''
        for i in range(len(p)):
            if p[i] == '(':
                left +=1
            else :
                right += 1
            u += p[i]
            
            if left == right :
                break
        v = p[i + 1:]
        
        if isPerfect(u):
            #print('%s is perfect' %(u))
            return u + func(v)
        else :
           
            u = list(u[1:-1])
            
            for i in range(len(u)):
                if u[i] == ')':
                    u[i] = '('
                else :
                    u[i] = ')'
            return '(' + func(v) + ')' + ''.join(u)
        
    if isPerfect(p):
        return p
        
    return func(p)
   