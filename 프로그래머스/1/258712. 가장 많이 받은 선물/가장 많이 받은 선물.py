def solution(friends, gifts):
    name = dict()
    numOfFriends = len(friends)
    presentFactor = [0] * numOfFriends
    numOfGetPresents = [0] * (numOfFriends)
    graph = [[0] * numOfFriends for _  in range(numOfFriends)]
    
    for i in  range(numOfFriends):
        name[friends[i]] = i

    
    for twoFriends in gifts :

        a = twoFriends.split(' ')
        u = a[0]
        v = a[1]
        presentFactor[name[u]] += 1
        presentFactor[name[v]] -= 1
        graph[name[u]][name[v]] += 1
  
      
    
   
    for A in range(numOfFriends) :
        for B in range(A + 1, numOfFriends) :
            
            # 받은 선물 개수가 같다면
            if graph[A][B] == graph[B][A] :
                
                if presentFactor[A] == presentFactor[B] :
                    continue
                elif presentFactor[A] > presentFactor[B] :
                    numOfGetPresents[A] += 1
                elif presentFactor[A] < presentFactor[B] :
                    numOfGetPresents[B] += 1
            # A가 더 많이 줬다면 
            elif graph[A][B] > graph[B][A] :
                numOfGetPresents[A] += 1
            # B가 더 많이 줬다면 
            elif graph[A][B] < graph[B][A] :
                numOfGetPresents[B] += 1
    
    
    answer = max(numOfGetPresents)
    return answer