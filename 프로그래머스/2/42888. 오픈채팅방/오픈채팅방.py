def solution(record):
    hash = dict()
    answer = []
    for r in record :
        r = r.split(" ")
        action = r[0]
        user = r[1]
        if action == 'Enter' or action == 'Change':
            name = r[2]
            hash[user] = name
        
    for r in record :
        r = r.split(" ")
        action = r[0]
        if action == 'Enter':
            answer.append("%s님이 들어왔습니다."%(hash[r[1]]))
        elif action == 'Leave':
            answer.append("%s님이 나갔습니다."%(hash[r[1]]))
    
    
    return answer