def solution(s):
    count = 0
    delete = 0
    while s!= '1':
        count += 1
        length = 0
        zero = 0
        for i in s :
            length += 1
            if i == '0':
                zero += 1
                delete += 1
        s = bin(length - zero)[2:]
        
    answer = []
    answer.append(count)
    answer.append(delete)
    return answer