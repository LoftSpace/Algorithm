from itertools import combinations
def solution(orders, course):
    answer = []
    for course_length in course :
        hash = dict()
        for order in orders:
            course_case = list(combinations(order,course_length))
            
            for case in course_case :
                a = list(case)
                a.sort()
                temp = ''.join(a)
                
                if temp in hash:
                    hash[temp] += 1
                else :
                    hash[temp] = 1
        #print(hash)
        Max = 0
        ans = []
        for i in hash :
            if hash[i] >=2 :
                if Max < hash[i] :
                    ans.clear()
                    ans.append(i)
                    Max = hash[i]
                elif Max == hash[i] :
                    ans.append(i)
        for i in ans :
            answer.append(i)
        
    answer.sort()
    return answer