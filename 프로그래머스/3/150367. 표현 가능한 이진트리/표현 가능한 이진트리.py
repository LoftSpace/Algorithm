import math

def solution(numbers):
    answer = []
    def check(arr,root,depth):
       
        if depth == 0 :
            return True
        elif arr[root] == '0':
            if arr[root - depth] == '1' or arr[root + depth] == '1':
                return False
        
        return check(arr,root - depth,depth //2) and check(arr,root + depth,depth//2)
        
    for number in numbers :
        arr = bin(number)[2:]
        N = len(arr)
        '''
        S = 1
        while S < N :
            S *= 2
        
        S -= 1
        #포화 이진트리 생성
        arr = '0' * (S - N) + arr
        '''
        h = math.ceil(math.log2(len(arr) + 1))
        size = 2 ** h - 1
        dummy = size - len(arr)
        arr = '0' * dummy + arr
        root = len(arr) // 2
        if check(arr,root,(root + 1)//2) :
            answer.append(1)
        else :
            answer.append(0)
        
        
    return answer