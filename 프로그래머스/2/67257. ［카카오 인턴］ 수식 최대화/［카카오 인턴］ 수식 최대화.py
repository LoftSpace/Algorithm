from itertools import permutations
def solution(expression):
    def calculate(a,op,b):
        if op == '-':
            return a-b
        elif op == '*':
            return a * b
        else :
            return a + b
    answer = 0
    operation = ['-','+','*']
    tokens = []
    operation_case = list(permutations(operation))
    token = ''
    for i in expression :
        if i== '-' or i == '+' or i == '*':
            tokens.append(int(token))
            tokens.append(i)
            token = ''
        else :
            token += i
    tokens.append(int(token))
    
    a = 0
    for case in operation_case:
        arr = tokens.copy()
        
        for op in case :
            stack = []
            while arr:
                #print(arr)
                temp = arr.pop(0)
                if temp == op :
                    stack.append(calculate(stack.pop(),op,arr.pop(0)))
                else :
                    stack.append(temp)
                
                a+=1

            arr = stack
        answer = max(answer,abs(stack[0]))
        
    
    return answer