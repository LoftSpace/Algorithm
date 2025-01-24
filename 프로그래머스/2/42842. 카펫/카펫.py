import math
def solution(brown, yellow):
    case = []
    for i in range(1,math.floor(math.sqrt(yellow)) + 1):
        if yellow % i == 0 :
            case.append([i,yellow//i])
    for i in case :
        border = (i[0] + i[1]) * 2 + 4
        if border == brown :
            return [i[1] + 2,i[0] + 2]
    answer = []
    return answer