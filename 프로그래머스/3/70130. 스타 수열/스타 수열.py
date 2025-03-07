def solution(a):
    hash = dict()
    answer = 0
    stack = []
    if len(a) == 1 :
        return 0
    elif len(a) == 2 :
        if a[0] != a[1] :
            return 1
        else :
            return 0
    #맨앞에 두개 같으면 하나 안셈
    if a[0] != a[1] :
        hash[a[0]] = 1
        
   
    if a[-1] != a[-2]:
        hash[a[-1]] = 1
            
    for i in range(1,len(a) - 1):
        if not(a[i-1] == a[i] and a[i] == a[i + 1]):
            if a[i] in hash :
                hash[a[i]] += 1
            else :
                hash[a[i]] = 1
                
    Key = -1
    count = 0
    for i in hash :
        if hash[i] > count :
            count = hash[i]
            Key = i
    #print(Key)
    for i in a :
        if i == Key :
            if stack :
                if stack[-1] != Key :
                    stack.clear()
                    answer += 1
            else :
                stack.append(i)
        else :
            if stack :
                if stack[-1] == Key :
                    stack.clear()
                    answer += 1
            else :
                stack.append(i)
    return answer * 2