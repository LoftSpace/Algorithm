from itertools import combinations
import math
def solution(weights):
    answer = 0
    hash = dict()
    for i in weights : 
        if i not in hash :
            hash[i] = 1
        else :
            hash[i] += 1

    for i in hash :
        if hash[i] > 1 :
            answer += math.comb(hash[i],2)
        if (i * 3) / 2 in hash :
            answer += hash[i] * hash[ (i * 3) / 2]
        if i * 2 in hash :
            answer += hash[i] * hash[i*2]
        if (i * 4) / 3 in hash :
            answer += hash[i] * hash[(i * 4) / 3]
    return answer