from itertools import combinations, product
def solution(dice):
    N = len(dice)
    dice_idx = list(range(0,len(dice)))
    nCr = combinations(range(N), N // 2)
    wins = []
    for caseA in nCr :
        caseB = [i for i in range(N) if i not in caseA]
        
        A, B = [], []
        for order_production in product(range(6),repeat = N//2) :
            A.append(sum(dice[i][j] for i, j in zip(caseA,order_production)))
            B.append(sum(dice[i][j] for i,j in zip(caseB, order_production)))
            
        B.sort()
      
        count = 0
        for num in A :
            left = 0
            right = len(B) - 1
            while left <= right :
                mid = (left + right) // 2
                if num > B[mid] :
                    left = mid + 1
                elif num <= B[mid] :
                    right = mid - 1
                
            count += left
        
        case = list(caseA)
        case.append(count)
        wins.append(case)
    
    answer = []
    Max = 0
    print(wins)
    for i in wins :
        if i[-1] > Max :
            Max = i[-1]
            answer = i
    for i in range(len(answer)-1) :
        answer[i] += 1
    print(answer[:-1])
    
    return answer[:-1]