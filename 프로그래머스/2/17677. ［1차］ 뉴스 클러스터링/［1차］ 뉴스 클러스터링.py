import math
def solution(str1, str2):
    characters = 'abcdefghijklmnopqrstuvwxyz'
    str1 = str1.lower()
    str2 = str2.lower()
    hash1 = dict()
    hash2 = dict()
    for i in range(len(str1)-1) :
        temp = ''
        if str1[i] in characters and str1[i + 1] in characters :
            temp += (str1[i] + str1[i + 1])
            if temp in hash1 :
                hash1[temp] += 1
            else :
                hash1[temp] = 1

    for i in range(len(str2)-1) :
        temp = ''
        if str2[i] in characters and str2[i + 1] in characters :
            temp += (str2[i] + str2[i + 1])
            if temp in hash2 :
                hash2[temp] += 1
            else :
                hash2[temp] = 1
    union = 0
    intersect = 0
    for i in hash1 :
        if i in hash2 :
            intersect += min(hash1[i],hash2[i])
            union += max(hash1[i],hash2[i])
        else :
            union += hash1[i]
    for i in hash2 :
        if i not in hash1 :
            union += hash2[i]

    if union == 0 :
        return 65536
    
    answer = math.floor((intersect / union) * 65536)
    return answer