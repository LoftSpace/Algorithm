import math
def solution(enroll, referral, seller, amount):
    graph = dict()
    count = dict()
    for person,parent in zip(enroll,referral) : 
        graph[person] = parent
        count[person] = 0
        
    
    def update_parent(person,amount):
        #print(amount)
        #부모가 있다면
        while person != '-' and amount > 0:
            #10%제외 자기가 갖는다
            #print('got %d'%(amount - math.floor(amount * 0.1)))
            count[person] += amount - math.floor(amount * 0.1)
            #부모로 이동
            person = graph[person]
            #print('give %d'%(math.floor(amount * 0.1)))
            amount = math.floor(amount * 0.1)
        
        #부모가 없다면
        #count[person] += amount * 
    
    for s,a in zip(seller,amount):
        update_parent(s,a * 100)
        #print(count)
    #print(count)
    answer = []
    for i in count:
        answer.append(count[i])
    
    return answer