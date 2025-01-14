from bisect import bisect_left
def solution(info, query):
    answer = []
    a = {"java":"0", "cpp":"1", "python":"2"}
    b = {"backend":"0", "frontend":"1"}
    c = {"junior":"0", "senior":"1"}
    d = {"chicken":"0", "pizza":"1"}
    hash = dict()
    
    for i in info :
        i = i.split(' ')
        key = ''
        key += (a[i[0]] + b[i[1]] + c[i[2]]) + d[i[3]]
        if key in hash :
            hash[key].append(int(i[4]))
        else :
            hash[key] = [int(i[4])]
    for i in hash :
        hash[i].sort()
    
    for q in query:
        #print(q)
        language, tech, position,food_and_score = q.split(' and ')
        food, score = food_and_score.split(' ')
        l = []
        t = []
        p = []
        f = []
        if language == '-':
            l.append('0')
            l.append('1')
            l.append('2')
        else :
            l.append(a[language])
        
        if tech == '-':
            t.append('0')
            t.append('1')
        else :
            t.append(b[tech])
        
        if position == '-':
            p.append('0')
            p.append('1')
        else :
            p.append(c[position])
            
        if food == '-' :
            f.append('0')
            f.append('1')
        else :
            f.append(d[food])
        count = 0
        for a1 in l:
            for a2 in t:
                for a3 in p:
                    for a4 in f:
                        temp = a1 + a2 + a3 + a4
                        if temp in hash :
                            
                            index = bisect_left(hash[temp],int(score))
                            count += len(hash[temp]) - index
                            #print(temp,hash[temp],index,score)
        answer.append(count)  
    return answer