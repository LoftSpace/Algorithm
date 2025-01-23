from itertools import combinations

def solution(relation):
    col_num = len(relation[0])
    row_num = len(relation)
    answer = []
    elements = set(i for i in range(col_num))
    
    for element_num in range(col_num + 1):
        keys = list(combinations(elements,element_num))
        #print(len(keys))
        for key in keys:
            key = list(key)
            tuples = []
            #각 row에 대해
            for row in range(row_num):
                tuple = []
                for i in key :
                    tuple.append(relation[row][i])
                #해당 튜플이 이미 존재하지 않는다면
                if tuple not in tuples :
                    tuples.append(tuple)
            if len(tuples) == row_num :
                answer.append(set(key))
    
    n = len(answer)
    answer2 = answer.copy()
    for i in range(n):
        for j in range(i + 1,n):
            set1 = answer[i]
            set2 = answer[j]
            if set1.issubset(set2):
                if set2 in answer2 :
                    answer2.remove(set2)
    return len(answer2)